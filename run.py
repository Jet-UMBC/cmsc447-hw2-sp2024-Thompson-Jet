# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:56:24 2024

@author: jetth
"""

from sqlite3 import connect
from flask import Flask, send_from_directory, g
import jinja2
from os.path import exists
from views.home import home
from views.update import update
from views.add import add
import database
import sqlite3

app = Flask(__name__)
app.debug = True;

@app.teardown_appcontext
def close_connection(exception):
    # close database
    db = getattr(g, '_database', None);
    if db is not None:
        db.close();
    #end if
#end CloseConnection()

app.register_blueprint(home)
app.register_blueprint(update)
app.register_blueprint(add)

if __name__ == '__main__':
    # application
    database.InitDatabase();
    app.run(port=8000, threaded=True)
