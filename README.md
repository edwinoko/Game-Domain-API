# Game-Domain-API
This project is basically a fighting game API. I will be creating smash bros api but also create scripts to have similar things built for other fighting games. This will then be used by the UFGP to generate the site and more. The database of the api is based on this layout but has a bit more then what is displayed here.

Setup

install the requirements and run 
uvicorn app.main:app --reload

In the browser you can go to the swagger page to test it out
http://127.0.0.1:8000/docs#/


## Fighting Game Data Folder Setup

For the setup of the game domain there needs to be some structure in which data is collected and stored. The setup should be something similar to the following

Data
- Archetypes
- Games
    - Game franchise e.g. Smash Bros Ultimate
        - Character file e.g. Falco.json

##
