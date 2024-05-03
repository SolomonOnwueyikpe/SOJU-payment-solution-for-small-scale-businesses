from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from wtforms import Form, StringField, PasswordField, validators
from flask_bootstrap import Bootstrap
import stripe

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STRIPE_PUBLIC_KEY'] = 'your_stripe_public_key'
app.config['STRIPE_SECRET_KEY'] = 'your_stripe_secret_key'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
stripe.api_key = app.config['STRIPE_SECRET_KEY']
Bootstrap(app)

