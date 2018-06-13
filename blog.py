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
    returnQueryBooks=Description.query.all();
    mybooks=[]
    #iterate through all the books
    for singleDescription in returnQueryBooks:
        mybooks.append(Book(singleDescription.bookname, singleDescription.date, singleDescription.tag, singleDescription.bookimage, singleDescription.endpoint))
    print mybooks
    return render_template('index.html', books=mybooks)

@app.route('/aboutUs')
def aboutUs():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/bookRenderPage/<booknamedb>')
def bookRenderPage(booknamedb):
    #database query to the book for the url provided
    returnQueryResult=Description.query.filter_by(endpoint=booknamedb).first()

    BookName = returnQueryResult.bookname
    bookImage=returnQueryResult.bookimage
    whereToBuy = returnQueryResult.wheretobuy
    AuthorName = returnQueryResult.authorname 

    AuthorDescription = returnQueryResult.authordescription
    bookIntro = returnQueryResult.bookintro
    FirstQuote = returnQueryResult.firstquote

    FirstQuoteAuthorName = returnQueryResult.firstquoteauthorname 
    QuestionsAskedToTheReader = returnQueryResult.questionsaskedtothereader 
    introToContent = returnQueryResult.introtocontent 
    questionContent = returnQueryResult.questioncontent

    SecondQuote = returnQueryResult.secondquote   
    SecondQuoteAuthorName = returnQueryResult.secondquoteauthorname 
    CloseBook = returnQueryResult.closebook 
    CallToAction = returnQueryResult.calltoaction

    return render_template(booknamedb+'.html', BookName=BookName, bookImage=bookImage, whereToBuy=whereToBuy, AuthorName=AuthorName, AuthorDescription=AuthorDescription, bookIntro=bookIntro, FirstQuote=FirstQuote, FirstQuoteAuthorName=FirstQuoteAuthorName, QuestionsAskedToTheReader=QuestionsAskedToTheReader, introToContent=introToContent, questionContent=questionContent, SecondQuote=SecondQuote, SecondQuoteAuthorName=SecondQuoteAuthorName, CloseBook=CloseBook, CallToAction=CallToAction)

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
    endpoint=db.Column(db.Text)
    bookname=db.Column(db.Text, primary_key=True)
    bookimage=db.Column(db.Text)
    tag=db.Column(db.Text)
    date=db.Column(db.Date)
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

class Book():
    def __init__(self, name, date, tag, image, endpoint):
        self.name=name
        self.date=date
        self.tag=tag
        self.image=image
        self.endpoint=endpoint

if __name__=="__main__":
    app.run(debug=True)