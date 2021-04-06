# Rest api


## DB Models
*listing*  
Has data for each listing, e.g.  
```
{
    id: 22911,  
    name: 'The Stuydio Modern and Light Filled',  
    host_id: 87773,  
    host_name: 'Shelly',  
    neighbourhood_group: 'Brooklyn',  
    neighbourhood: 'Bedford-Stuyvesant',  
    latitude: '40.684129999999996',  
    longitude: '-73.92357',  
    room_type: 'Entire home/apt',  
    price: 125,  
    minimum_nights: 7,  
    number_of_reviews: 139,  
    last_review: 2018-10-27T22:00:00.000Z,  
    reviews_per_month: '1.23',  
    calculated_host_listing_count: 2,  
    availability_365: 311  
}
```
*review*  
Data for a specific review, e.g.
```
{
    "listing_id": 2539, // Foreign Key listing   
    "review_id": 55688172,  
    "date": "2015-12-03T23:00:00.000Z",  
    "reviewer_id": 25160947,  
    "reviewer_name": "Peter",  
    "comments": "Great host "  
}
```

## Queries
### Adding Search Params
To add a search param to a request use ```COLUMNNAME.OPERATOR=VALUE```, where `COLUMNNAME` is a columnname as defined in the db models section. `OPERATOR` can take the following values: eq for =, ge for >=, le for <=. `VALUE` is the value you want to send, note that if the value is a string you must enclose it in '' e.g. `'a string'`  
To add search params to a GET request use `URL?COLUMNNAME.OPERATOR=VALUE`, e.g. `http://localhost:8888/listings?latitude.le=70`. To chain search parameters use & e.g.`http://localhost:8888/listings?latitude.le=70&longitude.eq=4`

### GET
**/**  
overview page.  

**/listings**  
returns all listing as json. Accepts search params.  
Example request: ```http://localhost:8888/listings```

**/listings/location**  
Returns the id, longitude and latitude of all listings. Accepts search params.  

Example Request:  ```http://localhost:8888/listings/location?longitude.ge=10&longitude.le=20&latitude.ge=-70&latitude.le=0```   

**listing/_ID_**  
returns all data for listing with _ID_. Doesn't accept search params.  
Example request: ```http://localhost:8888/listing/2539```  
  
**/listing/_ID_/reviews**  
returns all reviews for listing with _ID_. Accepts search params.  
Example request: ```http://localhost:8888/listing/2539/reviews```  
  
**/listing/_ID_/review/_REVIEWID_**  
returns review with id _REVIEWID_ for listing with id _ID_. Doesn't accept search params.  
Example request: ```http://localhost:8888/listing/2539/review/55688172```    

## Setup
Since github does not allow large files I splitted the db dump into multiple files.

0. Create an .env file, copy paste the following and add your infos to it:

PORT = 8888  
DB_HOST = localhost  
DB_USER = YOUR_POSTGRES_USER_NAME  
DB_PASSWORD = YOUR_POSTGRES_PASSWORD  
DB_NAME = YOUR_DB_NAME  
DB_PORT= YOUR_POSTGRES_PORT  

if you use docker:
1. go to /db and execute assembleDump.py
    -> the file pg_dump.sql should appear in this folder
2. come back here and use "docker compose up"
    -> rest_api and db should be built and run
    -> access rest_api via browser on "http://localhost:8888/", there you will find an overview

if you use node directly:
1. Go into the setupDB folder, modify the setupDB.py file so that it connects to your database
2. download the necessary data and store them in a new directory called data
3. execute setup.py
4. go into the rest_api folder and use `npm install`
5. use `npm start` 
