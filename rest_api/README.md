# Rest api

## Setup
Since github does not allow large files I splitted the db dump into multiple files.

0. Create an .env file and copy paste the following:

PORT = 8888
DB_HOST = postgres
DB_USER = ase_user
DB_PASSWORD = aseisgreat
DB_NAME = ase
DB_PORT= 5432

1. go to /db and execute assembleDump.py
    -> the file pg_dump.sql should appear in this folder
2. come back here and use "docker compose up"
    -> rest_api and db should be built and run
    -> access rest_api via browser on "http://localhost:8888/", there you will find an overview
