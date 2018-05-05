from flask import Flask, render_template, request, make_response, redirect, abort
from flask_bootstrap import Bootstrap

app=Flask(__name__)
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
	bookImage='richdadpoordad.jpg'
	return render_template('richDadPoorDad.html', bookImage=bookImage)

@app.route('/ComoFazerAmigosEINfluenciarPessoas')
def ComoFazerAmigosEINfluenciarPessoas():
    bookImage='ComoFazerAmigosEINfluenciarPessoas.jpg'
    return render_template('ComoFazerAmigosEINfluenciarPessoas.html', bookImage=bookImage)

@app.route('/DOTCOM')
def DOTCOM():
    bookImage='DOTCOM.jpg'
    return render_template('DOTCOM.html', bookImage=bookImage)

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