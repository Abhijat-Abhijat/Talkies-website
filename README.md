# Talkies---Website
### This is the repository for movie site project for Industrial training project.

- This repository contains the code for the framework of the site and the front-end has been forked from [Abhijat's repository](https://github.com/Abhijat-Abhijat/Talkies---Website). 

### The project has been created using the following technologies
- Front-end
  - HTML
  - CSS
  - JavaScript 
- Backend
  - MongoDB for the database
- Framework 
  - Django 
  - Djongo 


### Deploying the project 

**The instructions are only for Linux based systems. I am using Arch Linux and some instructions might be Arch Linux specific and you can find the equivalent instructions for your distribution accordingly.**

- First make sure python is installed on your system. Once done, install the virtualenv with `pip install virtualenv`.
- Now clone this repository to your required location with `git clone https://www.github.com/ghostx31/Talkies---Website` 
- Change directory into the repository and make sure MongoDB is installed. This instruction is Arch Linux specific and you can find the instructions for your distribution on MongoDB's website. Using your AUR helper, install the following packages from the AUR: `mongodb-bin`, `mongodb-tools-bin` and `mongodb-compass`. I am using paru so the command will be `paru -S monogdb-bin mongodb-tools-bin mongodb-compass`. 
- Now activate the virtual environment by typing `source bin/activate`. Add the suffix for your shell if using any shell other than bash. Example, for the fish shell, the command is `source bin/activate.fish`. 
- Now cd into `talkies/`. 
- **Since the database is present in my system locally, you will not have access to the database yet. So the site will not work completely.**
- Create a localhost instance using MongoDB Compass and edit the database section in settings.py accordingly. 
- Now run `python manage.py makemigrations` and `python manage.py migrate` to populate the database. 
- The project is now setup and data can be added to the database for the functioning of the project. 


**NOTE: The project is still a work in progress and things may break anytime.**
