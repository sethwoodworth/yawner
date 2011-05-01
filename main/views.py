from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from yawner.main.models import *

def home(request):
    """
    return this week in Yawnlog stats from site, maybe some social feeds (js?)
    TODO: add stats function
    TODO: add twitter feed
    """
    render_to_response('front.html', {} )
    
#@login_required
def dashboard(request):
    """
    Show last 7 days of stats as graph, show friend activity.
    TODO: friend activity
    """
    # the past week of sleep
    week_sleeps = Sleep.objects.filter(User=request.user).reverse()[:7]

    render_to_response('dashboard.html', {
        'sleeps':   week_sleeps,
        'user':     request.user,
        })
