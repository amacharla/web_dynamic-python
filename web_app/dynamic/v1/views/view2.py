#!/usr/bin/python3
"""View 2 Routes"""

from flask import Flask, Blueprint, jsonify
from dynamic.v1.views import app_views

@app_views.route('/2')
def hello_view_2():
        """placeholder for view 2"""
        return jsonify({"View 2": "OKAY"})
