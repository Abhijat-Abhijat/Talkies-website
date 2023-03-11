# Talkies Website

Talkies is a website where users can rate and watch movies and download them. The website

features carousels made with swiper.js and uses Tilt.js for enhanced visual effects. Trailers for

movies are fetched from YouTube, and the backend is powered by MongoDB and Mongoose.

The website is built using HTML, CSS, and JavaScript, with the Python Django framework.

## **Technologies Used**

• HTML

• CSS

• JavaScript

• Python Django

• MongoDB

• Mongoose

• swiper.js

• Tilt.js

• YouTube API


## **Setup**

To run the Talkies website, follow these steps:

1\. Clone the repository from GitHub.

2\. Install the required dependencies by running **pip install -r requirements.txt**.

3\. Start the Django server by running **python manage.py runserver**.

4\. Open your web browser and navigate to [**http://localhost:8000**](http://localhost:8000/)[** ](http://localhost:8000/)to access the website.

## **Deploying the project**

**The instructions are only for Linux based systems. I am using Arch Linux and some instructions might be Arch Linux specific and you can find the equivalent instructions for your distribution accordingly.**

• First make sure python is installed on your system. Once done, install the virtualenv with pip install virtualenv.

• Now clone this repository to your required location with git clone
<https://github.com/Abhijat-Abhijat/Talkies-website.git>

• Change directory into the repository and make sure MongoDB is installed. This instruction is Arch Linux specific, and you can find the instructions for your distribution on MongoDB's website. Using your AUR helper, install the following packages from the AUR: mongodb-bin, mongodb-tools-bin, and mongodb-compass. I am using paru so the command will be paru -S mongdb-bin mongodb-tools-bin mongodb-compass.

• Now activate the virtual environment by typing source bin/activate. Add the suffix for your shell if using any shell other than bash. Example, for the fish shell, the command is source bin/activate.fish.

• Install all the dependencies of the project using the requirements.txt file. The command is pip install -r requirements.txt.

• Now cd into talkies/.

**Since the database is present in my system locally, you will not have access to the database yet. So, the site will not work completely.**

• Create a localhost instance using MongoDB Compass and edit the database section in settings.py accordingly.

• Now run python manage.py collectstatic to collect the static files.

• Create a database in the local server of Mongo with the name talkies and add a collection home\_moviefiles.


• Then run python manage.py makemigrations and then python manage.py migrate to
populate the database.

• The project is now set up and data can be added to the database for its functioning.

**NOTE: The project is still a work in progress and things may break anytime.**

## **Features**

The Talkies website offers the following features:

• User authentication: Users can create an account and log in to rate movies and save their favorite movies.

• Movie ratings: Users can rate movies on a scale of 1 to 10.

• Movie watching: Users can watch movies directly on the website.

• Movie downloading: Users can download movies from the website.

• Trailers: Trailers for movies are fetched from YouTube and displayed on the website.

• Carousels: The website features carousels made with swiper.js for enhanced user experience.

• Visual effects: Tilt.js is used to add visual effects to the website.

## **Conclusion**

Talkies is a full-featured movie rating and watching website built with HTML, CSS, and JavaScript, powered by the Python Django framework, and backed by MongoDB and Mongoose. With its user authentication, movie ratings, watching and downloading capabilities,and YouTube trailer integration, Talkies provides a comprehensive movie experience for users.

