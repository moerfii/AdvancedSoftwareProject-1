scripts loads data from data folder and puts it into postgres

since files are too large you have to download them yourself from the following links
kaggle listings:
https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data?select=AB_NYC_2019.csv
full text reviews:
http://data.insideairbnb.com/united-states/ny/new-york-city/2019-07-08/data/reviews.csv.gz

for the script you need pandas,sqlalchemy and psycopg2.
if psycopg2 fails to install try psycopg2-binary 