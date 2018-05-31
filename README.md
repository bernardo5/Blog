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

## Creation of Postgres docker image and Database

1. ``` docker run --name postgresdocker -e POSTGRES_PASSWORD=pass -d postgres ```

2. Access the docker itself --> ``` docker exec -it postgresdocker psql -U postgres ``` where ``` postgresdocker ``` is the name of the container and ``` postgres ``` is the user

3. You should now be in the command line interface of the database inside the docker container.

4. Create the database for the website --> ``` create database honestlibraryreviewsDB; ```

5. Connect to the created database --> ``` \c honestlibraryreviewsdb; ```

6. Create the desired tables and insert the values: 

* Table creation: ``` CREATE TABLE Description(BookName text, BookImage text, whereToBuy text, AuthorName text, AuthorDescription text, bookIntro text, FirstQuote text, FirstQuoteAuthorName text, QuestionsAskedToTheReader text, introToContent text, questionContent text, SecondQuote text, SecondQuoteAuthorName text, CloseBook text, CallToAction text); ```

* Values Insertion (1): 

``` 
insert into Description(BookName, BookImage, whereToBuy, AuthorName, AuthorDescription, bookIntro, FirstQuote, FirstQuoteAuthorName, QuestionsAskedToTheReader, introToContent, questionContent, SecondQuote, SecondQuoteAuthorName, CloseBook, CallToAction) values ('Rich Dad Poor Dad', 'richdadpoordad.jpg', 'As you can see in the photo, my version of the book is a Portuguese translated version. Worldwide, you can get this book from normal online bookstores.', 'Robert T. Kiyosaki', 'Author and motivational conference man, Robert is known worldwide as a defensor of financial education. He is the founder of Rich Dad Company, one of the creators of the CASHFLOW educational game and is the author of several bestsellers.', 'Hello everyone! It\’s February post time! The book I\’ll be reviewing this month is called \“Rich Dad Poor Dad\", written by Robert T. Kiyosaki. It was self-published in 1997 and after being picked up commercially, it became a New York Times bestseller.', '\“In school we learn that mistakes are bad, and we are punished for making them. Yet, if you look at the way humans are designed to learn, we learn by making mistakes. We learn to walk by falling down. If we never fell down, we would never walk.\”', ' ','Are you tired of following supposed experts in investments and ending up losing all your money? You want to be financially secure but you don\’t know how to invest, simply don\’t know how the investments work, or you already thought about investing to save extra money, but all you always heard the news talking about is crashes, bad advices and bankrupt. Also, it is very common to heard about get rich quick schemes that all they do is getting people money, right?', 'In his book, Robert T. Kiyosaki tells you his unique economic perspective. He doesn\’t tell you, however, exactly set-by-step what you should invest on. He tells you his story about how he developed his perspective based on the advices from his two fathers – a highly educated father, fiscally poor, and his father\’s best friend, a eighth-grade dropout and self-made millionaire.', 'Now you\’re probably thinking… \“well, this all looks awesome…but there\’s no way I\’m going to get rich…\”. What this book told me is that everyone has its own financial problems, no matter how much money they have. For some is the problem of paying all the bills, for others is the fact that everyone is trying to get money from them. Why not focusing on solving your current financial problems? After that, you\’ll manage to get extra money, and then you\’ll have to deal with other kind of problems.', '\“Winners are not afraid of losing. But losers are. Failure is part of the process of success. People who avoid failure also avoid success.\”', ' ', 'The book talks about ways of developing your financial IQ and ways of becoming wealthier by being able to deal with the problems you encounter in a daily basis. This advices still stick no matter the economy, stocks or real estate.', 'If you are looking for ways to solve your financial problems, this book is for you. No matter how much money you have in your bank account, I\’m sure you\’ll find some good tips that will certainly apply to you.'); 
```

* Values Insertion (2): 

```
insert into Description(BookName, BookImage, whereToBuy, AuthorName, AuthorDescription, bookIntro, FirstQuote, FirstQuoteAuthorName, QuestionsAskedToTheReader, introToContent, questionContent, SecondQuote, SecondQuoteAuthorName, CloseBook, CallToAction) values ('How to make friends and Influence People', 

'ComoFazerAmigosEINfluenciarPessoas.jpg', 

'you can get this book in pretty much every book store.', 

'Dale Carnegie', 

'Dale Carnegie was born in 1888 in Missouri. He was a son of poor farmers and spent his childhood studying by performing great sacrifices. After finishing his studies he became a salesman. After he got tired of jobs in the sales area, he tried an artistic career in New York which was a failure. With no job and living in YMCA, he proposed himself to give motivational courses in exchange of fees. This idea proved to be a success and he has now an empire spread all over the world in this area.', 

'Hello everyone! Here comes a week bonus! This week, I managed to read two books, and instead of keeping it for later, I feel like sharing this book with you right now! Stay tuned!', 

'\“Any fool can criticise, complain, and condemn—and most fools do. But it takes character and self-control to be understanding and forgiving.\”', 

' ',

'You probably have encountered a moment in your life where someone gets favoured in a situation that you feel your skills are better than his/hers, right? Then why does this kind of situations occur? Or maybe, someone is being rude to you, you start arguing with them, and before you know it, you’re both fighting and you are being rude as well… Weird right? In the end, you just punished yourself and your goal was not achieved…', 

'Bearing similar thoughts in mind, and since the only way to make people behave in a certain manner is if they want to, Dale Carnegie knew that the ultimate key to success in almost every activity is to invest in relating to other people. The book starts with 3 ways of dealing with people and proposes 6 approaches to make people like you, following up to 12 ways of convincing them and 9 to become a leader. Manipulation? Maybe…Maybe not… Let\’s take a look into some core lessons present in the book.', 

'1.Avoid criticizing, condemning, or complaining;\n2.Praise others\’ achievements;\n3.Be empathetic;\n4.Know the value of charm;\n5.Encourage people to talk about themselves;\n6.Know when to use suggestions, instead of direct orders;\n7.Get others to think their conclusion is their own;\n8.Acknowledge your own mistakes;\n9.Respect others\’ dignity;\n10.Be friendly, no matter how angry this person may be;\n11.Reach common ground as soon as possible;\n12.Don’t try winning an argument.\nMost of them are common sense right? You’d be surprised about the kind of examples inside the book that you can relate to and you realize you\’re just passing right through them in your daily life… I mean…who doesn\’t like to be heard by friends, receive smiles and HONEST compliments and suggestions instead of orders? Right? Now think about it…How many times do you do that to others without second intentions? Shouldn\’t that be something to invest in? Wouldn\’t the world be a better place if everyone invested time in making other people\’s lives brighter?', 

'\“You can make more friends in two months by becoming interested in other people than you can in two years by trying to get other people interested in you.\”', 

' ', 

'Honestly, I was a bit skeptical about this book due to its title. It got me the idea that the content would be a bunch of mind hacks to get things out of people. Later on, I was talking to some friends of mine that constantly work on personal development, and trusting their word I invested in buying this book. They assured me that although this book could have a strong application in sales and business, it would be extremely valuable for people that just want to relate to others and improve their personal relationships. And guess what…you can succeed on the business part if you genuinely care about your relationships either they are customers or business partners.', 

''); 
```

* Values insertion (3):

```
insert into Description(BookName, BookImage, whereToBuy, AuthorName, AuthorDescription, bookIntro, FirstQuote, FirstQuoteAuthorName, QuestionsAskedToTheReader, introToContent, questionContent, SecondQuote, SecondQuoteAuthorName, CloseBook, CallToAction) values (

'DOTCOM SECRETS', 

'DOTCOM.jpg', 

'I got it in 2017 from a facebook targeted post, where i got a free+shipping offer. My advice is that if you want to read the book, follow Russell and send him a DM.', 

'Russel Brunson', 

'\"Russell started his first online company in college. Within a year of graduation he had sold over a million dollars of his own products and services from his basement. For over 10 years now he’s been helping companies double their traffic, conversions, and sales online.\"', 

'Hello everyone! The first book review of the year is about a book called \“DOTCOM SECRETS\”, written by Russell Brunson. In a few words, and as Tony Robbins commented: \“A simple process that ANY company can use to geometrically improve their traffic, conversation and sales online\”.', 

'\“A simple process that ANY company can use to geometrically improve their traffic, conversation and sales online\”', 

'Tony Robbins',

'Have you ever been in a situation where someone approaches you and they did not make the first selling move yet but you already feel uncomfortable? What is your very first reaction when they make you a yes or no question (supposing they actually reach that point…)? A huge \“NO!\”, right? The same stuff happens online right? You probably already have your own spam filter when you first open a website. The first seconds are crucial for you to decide whether or not you\’ll continue in the webpage to buy a product.', 

'So… What if you could target your product only to the people that can actually benefit from your product? What if they were only presented with a better offer after they find the first one actually worth of their money? If it was you, wouldn\’t that make you believe more in the seller and be more receptive to their product? I mean…you had already saw with your own eyes that their initial product shows results in your organisation… Why not perform an upgrade?', 

'This book gives great tips on how to relate to your customers online from the starting point where you define to whom your product is meant for, until the final phase where you provide maximum value to them. It all comes to providing value to the customer. The traffic increase and online sales come naturally.', 

' ', 

' ', 

'If you are a business man or if you’re thinking about launching a new business online of any kind, this is MUST for you to read. The tips given apply to any type of business.', 

' '); 
```

This method to perform insertions is definitely not the most appropriate one... It is intended the addition of an admin page to perform the insertions in the database... However... this is just the fastest way to put the blog up and running.


### Database Tables

You can access the database diagram in the ``` PostGresDatabase.pdf ``` file. **This document is not an E-R model**.

The tables disposition is now the following:

_Description:(**BookName**, BookImage, whereToBuyBook, AuthorName, AuthorDescription, bookIntro, FirstQuote, FirstQuoteAuthorName, QuestionsAskedToTheReader, introToContent, questionContent, SecondQuote, SecondQuoteAuthorName, CloseBook, CallToAction)_



