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
### GET
**/**  
overview page.  

**/listings**  
returns all listing as json
Example request: ```http://localhost:8888/listings```

**/listings/location**  
Returns the id, longitude and latitude of all listings.  

Accepts the following Search parameters for longitude and latitude:  
lat1, lat2, lon1, lon2. If they are not specified they will be set to 
either -180 (lat1, lon1) or 180(lat2, lon2). The query will then return
all listings between lat1 and lat2 and between lon1 and lon2.  
Example Request:  ```http://localhost:8888/listings/location?lon1=10&lon2=20&lat1=-70&lat2=0```   

**listing/_ID_**  
returns all data for listing with _ID_.  
Example request: ```http://localhost:8888/listing/2539```  
  
**/listing/_ID_/reviews**  
returns all reviews for listing with _ID_.  
Example request: ```http://localhost:8888/listing/2539/reviews```  
  
**/listing/_ID_/review/_REVIEWID_**  
returns review with id _REVIEWID_ for listing with id _ID_.  
Example request: ```http://localhost:8888/listing/2539/review/55688172```    
## Setup
Since github does not allow large files I splitted the db dump into multiple files.

0. Create an .env file and copy paste the following:

PORT = 8888  
DB_HOST = localhost  
DB_USER = ase_user  
DB_PASSWORD = aseisgreat  
DB_NAME = ase  
DB_PORT= 5432  

1. go to /db and execute assembleDump.py
    -> the file pg_dump.sql should appear in this folder
2. come back here and use "docker compose up"
    -> rest_api and db should be built and run
    -> access rest_api via browser on "http://localhost:8888/", there you will find an overview
