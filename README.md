# Blog

## Purpose

* This project came up as a way to learn flask with a real problem.

* My current blog (https://honestlibraryreviews.wordpress.com/) has the reviews of the books I have been reading in 2018 but it is hosted in wordpress and I have not written a single line of code for it.

* This project aims to replicate the Wordpress blog using Flask.

## Features to be made available

* Host the book reviews in a similar way of the original website

* Have admin page to insert new reviews

## How it will be accomplished

* Site hosting in AWS

* Database to save logins and text content of the books

How the site will work:

* Landing page will fetch all the available books in the DB and present its images, titles and month of the review

* When a book is selected, the backend fetches the text and images associated with the book and switches to the correspondant book page

## How to run this code

Installation requirements:

1. Install VirtualEnv --> ```sudo apt-get install python-virtualenv```

2. Name your virtualenv to work on --> ```virtualenv <name>```

3. Activate it --> ```source <name>/bin/activate```

4. Install Flask --> ```pip install Flask```

5. Install Bootstrap --> ```pip install flask-bootstrap```

To run the code:

1. Clone the repository

2. Export the blog.py file --> ```export FLASK_APP=blog.py```

3. Run the application --> ```flask run```

4. Open Google Chrome and access ```http://127.0.0.1:5000/```

For developer mode use ```export FLASK_ENV=development```
