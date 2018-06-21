# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
# functions based view
"""def home_old(request):
    html_ =<!DOCTYPE html>
    <html lang="en">
    <head>
    </head>
    <body>
    <h1>Hello World!</h1>
    <p>This is html coming through HI ! :) :)</P>
    </body>
    </html>
return HttpResponse({html_})
"""
#return render(request, "home.html",{} )#response

def home(request):
    return render(request, "base.html", {})#response