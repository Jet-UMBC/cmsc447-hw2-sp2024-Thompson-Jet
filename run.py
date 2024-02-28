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

app = Flask(__name__)

def GetDatabase():
    pass;
#end GetDatabase()

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

if __name__ == '__main__':
    # application
    app.run(port=8000, threaded=True)
