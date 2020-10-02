from datetime import datetime, timedelta, date

from flask import render_template, request

from app.public import public_mod
from app.public.models import *


@public_mod.route('/')
def index():
    return render_template("public/index.html")


