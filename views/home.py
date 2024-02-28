# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:02:54 2024

@author: jetth
"""

from flask import Blueprint, render_template, abort, request, make_response, redirect, Response;
from jinja2 import TemplateNotFound;

home = Blueprint("home", __name__, url_prefix="/");

@home.route("/", methods=["GET", "POST"])
def index():
    try:
        if(request.method == "POST"):
            print(request.form);    
        #end if
        
        return render_template(
            "home/index.html",
            title="Home",
            tableData=[("Jet", 1337, 200)],
            );
    except TemplateNotFound:
        abort(404);
    #end try
#end index()