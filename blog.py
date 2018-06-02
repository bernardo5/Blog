from flask import Flask, render_template, request, make_response, redirect, abort
from flask_bootstrap import Bootstrap
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:pass@localhost:5432/honestlibraryreviewsdb'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

app.debug=True
bootstrap=Bootstrap(app)

@app.route('/')
def landingPage():
	return render_template('index.html')

@app.route('/aboutUs')
def aboutUs():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/richDadPoorDad')
def richDadPoorDad():
    #database query to the book for the url provided
    returnQueryResultRichDadPoorDad=Description.query.filter_by(bookname="Rich Dad Poor Dad").first()

    BookName = returnQueryResultRichDadPoorDad.bookname
    bookImage=returnQueryResultRichDadPoorDad.bookimage
    whereToBuy = returnQueryResultRichDadPoorDad.wheretobuy
    AuthorName = returnQueryResultRichDadPoorDad.authorname 

    AuthorDescription = returnQueryResultRichDadPoorDad.authordescription
    bookIntro = returnQueryResultRichDadPoorDad.bookintro
    FirstQuote = returnQueryResultRichDadPoorDad.firstquote

    FirstQuoteAuthorName = returnQueryResultRichDadPoorDad.firstquoteauthorname 
    QuestionsAskedToTheReader = returnQueryResultRichDadPoorDad.questionsaskedtothereader 
    introToContent = returnQueryResultRichDadPoorDad.introtocontent 
    questionContent = returnQueryResultRichDadPoorDad.questioncontent

    SecondQuote = returnQueryResultRichDadPoorDad.secondquote   
    SecondQuoteAuthorName = returnQueryResultRichDadPoorDad.secondquoteauthorname 
    CloseBook = returnQueryResultRichDadPoorDad.closebook 
    CallToAction = returnQueryResultRichDadPoorDad.calltoaction

    return render_template('BookBase.html', BookName=BookName, bookImage=bookImage, whereToBuy=whereToBuy, AuthorName=AuthorName, AuthorDescription=AuthorDescription, bookIntro=bookIntro, FirstQuote=FirstQuote, FirstQuoteAuthorName=FirstQuoteAuthorName, QuestionsAskedToTheReader=QuestionsAskedToTheReader, introToContent=introToContent, questionContent=questionContent, SecondQuote=SecondQuote, SecondQuoteAuthorName=SecondQuoteAuthorName, CloseBook=CloseBook, CallToAction=CallToAction)

@app.route('/ComoFazerAmigosEINfluenciarPessoas')
def ComoFazerAmigosEINfluenciarPessoas():
    #database query to the book for the url provided
    returnQueryResultRichDadPoorDad=Description.query.filter_by(bookname="How to make friends and Influence People").first()

    BookName = returnQueryResultRichDadPoorDad.bookname
    bookImage=returnQueryResultRichDadPoorDad.bookimage
    whereToBuy = returnQueryResultRichDadPoorDad.wheretobuy
    AuthorName = returnQueryResultRichDadPoorDad.authorname 

    AuthorDescription = returnQueryResultRichDadPoorDad.authordescription
    bookIntro = returnQueryResultRichDadPoorDad.bookintro
    FirstQuote = returnQueryResultRichDadPoorDad.firstquote

    FirstQuoteAuthorName = returnQueryResultRichDadPoorDad.firstquoteauthorname 
    QuestionsAskedToTheReader = returnQueryResultRichDadPoorDad.questionsaskedtothereader 
    introToContent = returnQueryResultRichDadPoorDad.introtocontent 
    questionContent = returnQueryResultRichDadPoorDad.questioncontent

    SecondQuote = returnQueryResultRichDadPoorDad.secondquote   
    SecondQuoteAuthorName = returnQueryResultRichDadPoorDad.secondquoteauthorname 
    CloseBook = returnQueryResultRichDadPoorDad.closebook 
    CallToAction = returnQueryResultRichDadPoorDad.calltoaction

    return render_template('BookBase.html', BookName=BookName, bookImage=bookImage, whereToBuy=whereToBuy, AuthorName=AuthorName, AuthorDescription=AuthorDescription, bookIntro=bookIntro, FirstQuote=FirstQuote, FirstQuoteAuthorName=FirstQuoteAuthorName, QuestionsAskedToTheReader=QuestionsAskedToTheReader, introToContent=introToContent, questionContent=questionContent, SecondQuote=SecondQuote, SecondQuoteAuthorName=SecondQuoteAuthorName, CloseBook=CloseBook, CallToAction=CallToAction)

@app.route('/DOTCOM')
def DOTCOM():
    #database query to the book for the url provided
    returnQueryResultRichDadPoorDad=Description.query.filter_by(bookname="DOTCOM SECRETS").first()

    BookName = returnQueryResultRichDadPoorDad.bookname
    bookImage=returnQueryResultRichDadPoorDad.bookimage
    whereToBuy = returnQueryResultRichDadPoorDad.wheretobuy
    AuthorName = returnQueryResultRichDadPoorDad.authorname 

    AuthorDescription = returnQueryResultRichDadPoorDad.authordescription
    bookIntro = returnQueryResultRichDadPoorDad.bookintro
    FirstQuote = returnQueryResultRichDadPoorDad.firstquote

    FirstQuoteAuthorName = returnQueryResultRichDadPoorDad.firstquoteauthorname 
    QuestionsAskedToTheReader = returnQueryResultRichDadPoorDad.questionsaskedtothereader 
    introToContent = returnQueryResultRichDadPoorDad.introtocontent 
    questionContent = returnQueryResultRichDadPoorDad.questioncontent

    SecondQuote = returnQueryResultRichDadPoorDad.secondquote   
    SecondQuoteAuthorName = returnQueryResultRichDadPoorDad.secondquoteauthorname 
    CloseBook = returnQueryResultRichDadPoorDad.closebook 
    CallToAction = returnQueryResultRichDadPoorDad.calltoaction

    return render_template('BookBase.html', BookName=BookName, bookImage=bookImage, whereToBuy=whereToBuy, AuthorName=AuthorName, AuthorDescription=AuthorDescription, bookIntro=bookIntro, FirstQuote=FirstQuote, FirstQuoteAuthorName=FirstQuoteAuthorName, QuestionsAskedToTheReader=QuestionsAskedToTheReader, introToContent=introToContent, questionContent=questionContent, SecondQuote=SecondQuote, SecondQuoteAuthorName=SecondQuoteAuthorName, CloseBook=CloseBook, CallToAction=CallToAction)

@app.route('/db')
def deb():
    returnQueryResult=Description.query.all()
    myList='Start: '
    for bookName in returnQueryResult:
        myList=myList + ' ' + str(bookName.bookname)
    return myList

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


class Description(db.Model):
    __tablename__ = 'description'

    bookname=db.Column(db.Text, primary_key=True)
    bookimage=db.Column(db.Text)
    wheretobuy=db.Column(db.Text)
    authorname=db.Column(db.Text)
    authordescription=db.Column(db.Text)
    bookintro=db.Column(db.Text)
    firstquote=db.Column(db.Text)
    firstquoteauthorname=db.Column(db.Text)
    questionsaskedtothereader=db.Column(db.Text)
    introtocontent=db.Column(db.Text)
    questioncontent=db.Column(db.Text)
    secondquote=db.Column(db.Text)
    secondquoteauthorname=db.Column(db.Text)
    closebook=db.Column(db.Text)
    calltoaction=db.Column(db.Text)

    def __repr__(self):
        return '<Book %r>' % self.bookname



if __name__=="__main__":
    app.run(debug=True)