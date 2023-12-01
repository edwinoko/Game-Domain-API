# Game-Domain-API
This project is basically a fighting game API. I will be creating smash bros api but also create scripts to have similar things built for other fighting games. This will then be used by the UFGP to generate the site and more. The database of the api is based on this layout but has a bit more then what is displayed here.

- Characters
    - Name
    - Game name
    - Introduced in
    - Link to backstory/More info like wiki page

- Moves
    - name
    - startup frames
    - active frame
    - Recovery frame
    - Cancel Frame
    - Cancel move
    - Game name
    - Image of move

- Balanced Archetypes
    - All-Rounder
    - Mix-Up
    - Bait & Punish
    - Grappler

- Offensive Archetypes
    - Glass Cannon
    - Rushdown
    - Footsies
    - Pressurer
    - Hit & Run
    - Zone-Breaker
    - Dominating

- Defensive Archetypes
    - Zoner
    - Trapper
    - Turtle
    - Keep Away
    - Stage Control
    - Tag Team

Setup

install the requirements and run 
uvicorn app.main:app --reload

In the browser you can go to the swagger page to test it out
http://127.0.0.1:8000/docs#/
