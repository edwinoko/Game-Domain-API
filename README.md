# Game-Domain-API
This project is basically a fighting game API. I will be creating smash bros api but also create scripts to have similar things built for other fighting games. This will then be used by the UFGP to generate the site and more. The database of the api is based on this layout but has a bit more then what is displayed here.

Setup run without docker

install the requirements and run 
uvicorn app.main:app --reload

In the browser you can go to the swagger page to test it out
http://127.0.0.1:8000/docs#/

With docker

docker build -t game-domain-api .

docker run -p 8000:8000 game-domain-api


## Fighting Game Data Folder Setup

For the setup of the game domain there needs to be some structure in which data is collected and stored. The setup should be something similar to the following

Data
- Archetypes
- Games
    - Game franchise e.g. Smash Bros Ultimate
        - Character file e.g. Falco.json

## Template for the Character file

{   "name": "Fox"
    "archetype": "['Rushdown']"
    "url": "/fox",
    "release_date": "2022-09-19 15:00:39.415696",
    "summary": "Is a Fox in space and he has a bird best friend. Irony much?"
    "moves": {
        "jab_1": {
            "name" = Column(String)
            "alias" = Column(String)
            "startup_frames" = Column(String)
            "landing_lag" = Column(String)
            "duration" = Column(String)
            "active_frame" = Column(String)
            "end_active_frame" = Column(String)
            "recovery_frames" = Column(String)
            "start_invincibility_frame" = Column(String)
            "end_invincibility_frame" = Column(String)
            "gif_link" = Column(String)
            "command_input" = Column(String)
            "base_damage" = 
            "notes" = Column(String)
            "shield_lag" = Column(String)
            "shield_stun" = Column(String)
            "extra_information" = Column(String)
            "cancellable" = Column(String)
        }
    }
}
