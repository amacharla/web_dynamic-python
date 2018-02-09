#!/usr/bin/python3
"""Initialize Blueprint views"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/dynamic/v1")

from dynamic.v1.views.view1 import *
from dynamic.v1.views.view2 import *
from dynamic.v1.views.view3 import *
