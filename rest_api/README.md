# Rest api


## DB Models
*listing_location*  
stores id, latitude, longitude 
example
```
{
    "id": 2539,
    "latitude": "40.647490000000005",
    "longitude": "-73.97237"
  
}
```
  
*listing_detail*
stores additional information relevant to the consumer
example
```
 {
    "id": 2539,
    "thumbnail_url": null,
    "medium_url": null,
    "picture_url": "https://a0.muscache.com/im/pictures/3949d073-a02e-4ebc-aa9c-ac74f00eaa1f.jpg?aki_policy=large",
    "xl_picture_url": null,
    "name": "Clean & quiet apt home by the park",
    "listing_url": "https://www.airbnb.com/rooms/2539",
    "price": 0,
    "summary": "Renovated apt home in elevator building.",
    "space": "Spacious, renovated, and clean apt home, one block to F train, 25 minutes to lower Manhatten",
    "description": "Renovated apt home in elevator building. Spacious, renovated, and clean apt home, one block to F train, 25 minutes to lower Manhatten Close to Prospect Park and Historic Ditmas Park Very close to F and G trains and Express bus into NY.  The B and Q are closeby also. If this room is unavailable on your desired dates, check out our other rooms, such as:  https://www.airbnb.com/rooms/10267242",
    "neighborhood_overview": "Close to Prospect Park and Historic Ditmas Park",
    "transit": "Very close to F and G trains and Express bus into NY.  The B and Q are closeby also.",
    "access": null,
    "host_id": 2787,
    "guests_included": 1,
    "number_of_reviews": 9
 }
```
  
*listing_other*
stores other information  
example  
```
{
    "id": 2539,
    "square_feet": 0,
    "property_type": "Apartment",
    "room_type": "Private room",
    "neighbourhood_cleansed": "Kensington",
    "neighbourhood_group_cleansed": "Brooklyn",
    "minimum_nights": 1,
    "maximum_nights": 730
}
```
  
*listing_reviews*
stores review ratings  
example  
```
{
    "id": 2539,
    "review_scores_rating": "98.0",
    "review_scores_accuracy": "10.0",
    "review_scores_cleanliness": "10.0",
    "review_scores_checkin": "10.0",
    "review_scores_communication": "10.0",
    "review_scores_location": "10.0",
    "review_scores_value": "10.0"
}
```
  
*host*
stores host data
example
```
{
    "host_id": 2787,
    "host_location": "New York, New York, United States",
    "host_is_superhost": "f",
    "host_neighbourhood": "Gravesend",
    "host_listings_count": 6,
    "host_total_listings_count": 6,
    "host_identity_verified": "t",
    "calculated_host_listings_count": 6,
    "calculated_host_listings_count_entire_homes": 0,
    "calculated_host_listings_count_private_rooms": 5,
    "calculated_host_listings_count_shared_rooms": 1
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
all GET requests can be expanded with `/ID` to get data for a specific id, naturally this query doesn't accept search parameters.   e.g. ```http://localhost:8888/listing_location/2539```  
  
  
**/**  
overview page. outdated  

**/listing_location**  
returns all location data. Accepts search params.  
Example requests:   
```http://localhost:8888/listing_location```  
```http://localhost:8888/listing_location?longitude.ge=-70&latitude.le=0```  
```http://localhost:8888/listing_location/2539```  
```
[
  {
    "id": 2539,
    "latitude": "40.647490000000005",
    "longitude": "-73.97237"
  }
]
```  

**/listing_detail**  
Connects to db with same name. 
Example reequests:  
```http://localhost:8888/listing_detail``` NOTE: Try not to use this, since it delivers over 100MB of data  
```http://localhost:8888/listing_detail?&price.le=100&guests_included.ge=2```   
```http://localhost:8888/listing_detail/2539```   
```
[
  {
    "id": 2539,
    "thumbnail_url": null,
    "medium_url": null,
    "picture_url": "https://a0.muscache.com/im/pictures/3949d073-a02e-4ebc-aa9c-ac74f00eaa1f.jpg?aki_policy=large",
    "xl_picture_url": null,
    "name": "Clean & quiet apt home by the park",
    "listing_url": "https://www.airbnb.com/rooms/2539",
    "price": 149,
    "summary": "Renovated apt home in elevator building.",
    "space": "Spacious, renovated, and clean apt home, one block to F train, 25 minutes to lower Manhatten",
    "description": "Renovated apt home in elevator building. Spacious, renovated, and clean apt home, one block to F train, 25 minutes to lower Manhatten Close to Prospect Park and Historic Ditmas Park Very close to F and G trains and Express bus into NY.  The B and Q are closeby also. If this room is unavailable on your desired dates, check out our other rooms, such as:  https://www.airbnb.com/rooms/10267242",
    "neighborhood_overview": "Close to Prospect Park and Historic Ditmas Park",
    "transit": "Very close to F and G trains and Express bus into NY.  The B and Q are closeby also.",
    "access": null,
    "host_id": 2787,
    "guests_included": 1,
    "number_of_reviews": 9
  }
]
```  

**listing_other**  
Connects to db with same name.   
Example request:  
```http://localhost:8888/listing_other```  
```http://localhost:8888/listing_other?square_feet.ge=100```  
```http://localhost:8888/listing_other/2539```  
```
[
  {
    "id": 2539,
    "square_feet": 0,
    "property_type": "Apartment",
    "room_type": "Private room",
    "neighbourhood_cleansed": "Kensington",
    "neighbourhood_group_cleansed": "Brooklyn",
    "minimum_nights": 1,
    "maximum_nights": 730
  }
]
```  

**listing_reviews**
Connects to db with same name.
```http://localhost:8888/listing_reviews```  
```http://localhost:8888/listing_reviews?review_scores_cleanliness.ge=5```  
```http://localhost:8888/listing_reviews/2539```  
```
[
  {
    "id": 2539,
    "review_scores_rating": "98.0",
    "review_scores_accuracy": "10.0",
    "review_scores_cleanliness": "10.0",
    "review_scores_checkin": "10.0",
    "review_scores_communication": "10.0",
    "review_scores_location": "10.0",
    "review_scores_value": "10.0"
  }
]
```  

**host**
Connects to db with same name.  
```http://localhost:8888/host```  
```http://localhost:8888/host?host_is_superhost='t'```  
```http://localhost:8888/host/2787```  
```
[
  {
    "host_id": 2787,
    "host_location": "New York, New York, United States",
    "host_is_superhost": "f",
    "host_neighbourhood": "Gravesend",
    "host_listings_count": 6,
    "host_total_listings_count": 6,
    "host_identity_verified": "t",
    "calculated_host_listings_count": 6,
    "calculated_host_listings_count_entire_homes": 0,
    "calculated_host_listings_count_private_rooms": 5,
    "calculated_host_listings_count_shared_rooms": 1
  }
]
```  

**/reviews**  
returns all reviews for listing with _ID_. Accepts search params.  
Example request: 
```http://localhost:8888/reviews``` NOTE: Too much data don't use this  
```http://localhost:8888/reviews?listing_id.eq=2595```  
```http://localhost:8888/listing/17857```  
```
[
  {
    "listing_id": 2595,
    "id": 17857,
    "date": "2009-11-20T23:00:00.000Z",
    "reviewer_id": 50679,
    "reviewer_name": "Jean",
    "comments": "\"Notre séjour de trois nuits.\r\nNous avons apprécier L'appartement qui est très bien situé. Agréable, propre et bien soigné. C'est idéal pour une famille de 3 ou 4 personnes.\r\nPetits soucis en arrivant il y avait personne pour nous recevoir, et il manquait le savon pour la douche, le liquide vaisselle, nous les avons reçu de surlendemain. Il y a aussi le bruit du Métro de NY, donc une première nuit difficile si on est pas habitué. Jennifer est correcte le remboursement de la caution était très rapide.  A part ces petits détails notre court séjour c'est bien passé. \r\nSi j'ai la possibilité de revenir sur NY pour les vacances, je reprendrai à \"\"The Midtown Castle\"\"\r\nJean\r\nPossession - Ile de La Réunion\r\n\""
  }
]
```  
  
**/search_address**
returns latitude and longitude for a given location   
Example request:
```http://localhost:8888/search_address?location=300%20Jay%20St,%20Brooklyn,%20NY%2011201,%20United%20States```  
```
{
  "lat": 40.695511,
  "lng": -73.987128
}
```
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
