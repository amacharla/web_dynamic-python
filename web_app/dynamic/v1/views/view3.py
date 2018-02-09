#!/usr/bin/python3
"""View 3 Routes"""

from flask import Flask, Blueprint, jsonify
from dynamic.v1.views import app_views

@app_views.route('/3')
def hello_view_3():
        """placeholder for view 3"""
        return jsonify({"View 3": "OKAY"})
