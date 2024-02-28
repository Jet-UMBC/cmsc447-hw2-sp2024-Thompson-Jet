# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 12:57:26 2024

@author: jetth
"""

from flask import Blueprint, render_template, abort, request, make_response, redirect, Response;
from jinja2 import TemplateNotFound;

update = Blueprint("update", __name__, url_prefix="/update");

@update.route("/", methods=["GET", "POST"])
def index():
    try:
        return render_template(
            "update/index.html",
            title="Update",
            );
    except TemplateNotFound:
        abort(404);
    #end try
#end index()

@update.route("/result/", methods=["GET"])
def result():
    try:
        return render_template(
            "update/result.html",
            title="Update Result",
            );
    except TemplateNotFound:
        abort(404);
    #end try
#end index()