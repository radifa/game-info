import os
import secrets
import pytz
from PIL import Image
from datetime import datetime
from flask import render_template, url_for, flash, redirect, request
from gameinfo import app, db, bcrypt
from gameinfo.forms import RegistrationForm, LoginForm, UpdateAccountForm, RenterForm, ReturnForm, SearchForm
from gameinfo.models import Game
from flask_login import login_user, current_user, logout_user, login_required

db.create_all()

@app.route("/", methods=['GET', 'POST'])
def begin():
    page = request.args.get('page', 1, type=int)
    games = Game.query.order_by(Game.rank.asc()).paginate(page=page, per_page=10)
    form2 = SearchForm(request.form)
    if request.method == 'POST':
        kata ='%' + form2.data['kata'].title() + '%'
        return redirect(url_for('search',kata=kata))
    return render_template('home.html', games=games, form2=form2)

@app.route("/home", methods=['GET', 'POST'])
def home():
    page = request.args.get('page', 1, type=int)
    games = Game.query.order_by(Game.rank.asc()).paginate(page=page, per_page=10)
    form2 = SearchForm(request.form)
    if request.method == 'POST':
        kata ='%' + form2.data['kata'].title() + '%'
        return redirect(url_for('search',kata=kata))
    return render_template('home.html', games=games, form2=form2)

@app.route("/search/<string:kata>", methods=['GET', 'POST'])
def search(kata):
    page = request.args.get('page', 1, type=int)
    hasil = Game.query.filter(Game.name.like(kata)).paginate(page=page, per_page=10)
    return render_template('search.html', title='Hasil Pencarian', hasil=hasil, kata=kata)

@app.route("/genre/<string:genre>", methods=['GET', 'POST'])
def genre_game(genre):
    page = request.args.get('page', 1, type=int)
    games = Game.query.filter_by(genre=genre).order_by(Game.rank.asc()).paginate(page=page, per_page=10, error_out=False)
    games2 = Game.query.filter_by(genre=genre).first()
    form2 = SearchForm(request.form)
    if request.method == 'POST':
        kata ='%' + form2.data['kata'].title() + '%'
        return redirect(url_for('search',kata=kata))
    return render_template('genre_game.html', games=games, games2=games2, form2=form2)

@app.route("/platform/<string:platform>", methods=['GET', 'POST'])
def platform_game(platform):
    page = request.args.get('page', 1, type=int)
    games = Game.query.filter_by(platform=platform).order_by(Game.rank.asc()).paginate(page=page, per_page=10, error_out=False)
    games2 = Game.query.filter_by(platform=platform).first()
    form2 = SearchForm(request.form)
    if request.method == 'POST':
        kata ='%' + form2.data['kata'].title() + '%'
        return redirect(url_for('search',kata=kata))
    return render_template('platform_game.html', games=games, games2=games2, form2=form2)

@app.route("/newest", methods=['GET', 'POST'])
def newest():
    page = request.args.get('page', 1, type=int)
    form2 = SearchForm(request.form)
    if request.method == 'POST':
        kata ='%' + form2.data['kata'].title() + '%'
        return redirect(url_for('search',kata=kata))
    games = Game.query.order_by(Game.year.desc()).paginate(page=page, per_page=10, error_out=False)
    return render_template('newest.html', games=games, form2=form2)

@app.route("/about", methods=['GET', 'POST'])
def about():
    form2 = SearchForm(request.form)
    if request.method == 'POST':
        kata ='%' + form2.data['kata'].title() + '%'
        return redirect(url_for('search',kata=kata))
    return render_template('about.html', title='About', form2=form2)

@app.route("/nasales", methods=['GET', 'POST'])
def nasales():
    form2 = SearchForm(request.form)
    if request.method == 'POST':
        kata ='%' + form2.data['kata'].title() + '%'
        return redirect(url_for('search',kata=kata))
    return render_template('nasales.html', title='NA Sales', form2=form2)

@app.route("/eusales", methods=['GET', 'POST'])
def eusales():
    form2 = SearchForm(request.form)
    if request.method == 'POST':
        kata ='%' + form2.data['kata'].title() + '%'
        return redirect(url_for('search',kata=kata))
    return render_template('eusales.html', title='EU Sales', form2=form2)

@app.route("/jpsales", methods=['GET', 'POST'])
def jpsales():
    form2 = SearchForm(request.form)
    if request.method == 'POST':
        kata ='%' + form2.data['kata'].title() + '%'
        return redirect(url_for('search',kata=kata))
    return render_template('jpsales.html', title='JP Sales', form2=form2)

@app.route("/otsales", methods=['GET', 'POST'])
def otsales():
    form2 = SearchForm(request.form)
    if request.method == 'POST':
        kata ='%' + form2.data['kata'].title() + '%'
        return redirect(url_for('search',kata=kata))
    return render_template('otsales.html', title='Other Sales', form2=form2)

@app.route("/glsales", methods=['GET', 'POST'])
def glsales():
    form2 = SearchForm(request.form)
    if request.method == 'POST':
        kata ='%' + form2.data['kata'].title() + '%'
        return redirect(url_for('search',kata=kata))
    return render_template('glsales.html', title='Global Sales', form2=form2)