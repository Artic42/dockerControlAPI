# dockerControlAPI
An API to be deployed in rapberry pi slaves and master in order to contorl the docker containers running on that server.


## Avilable endpoints 

### /API/build

Send a dockerfile in the body, the system will build it and return with the complete log of the building procedure.

### /API/deployed

Send a docker compose file, it will set up the docker compose up the file

### /API/stop

Send a docker compose file, it will stop the docker compose file

### /API/status

It sends the respones od the _docker ps --all_ commmand

### /API/images

It sends a list of the existing images in the server