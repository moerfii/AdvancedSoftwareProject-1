# Fairbnb

This folder holds the FairBNB application.  
`frontend/` holds the code used for the frontend  
`kivymd/` holds kivy specific dependencies.  
`restAPIConnection/` holds the code for the stand-alone class used to communicate with the REST API.  
`main.py` is used to start the application.

## Quickstart
### Python
* use `pip install -r requirements.txt` for the dependencies
* use `python main.py start` to start the application. or `python main.py test` to execute the test.

### Docker (UNIX only)
* build the application with `docker build -t FairBNB`
* run the application with `sudo docker run -it --expose PORT -e DISPLAY=$DISPLAY --user 1000 --network="host" FairBNB`, where `PORT` is the port 
where the REST API runs (if the rest api runs on another computer omit it).
 
