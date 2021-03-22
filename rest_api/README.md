# Rest api

## Setup
Since github does not allow large files I splitted the db dump into multiple files.

1. go to /db and execute assembleDump.py
    -> the file pg_dump.sql should appear in this folder
2. come back here and use "docker compose up"
    -> rest_api and db should be built and run
    -> access rest_api via browser on "http://localhost:8888/", there you will find an overview
