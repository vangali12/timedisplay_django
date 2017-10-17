# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def displayTime(request):
	context = {
	"date": strftime("%Y-%m-%d", gmtime()),
	"time": strftime("%H:%M %p", gmtime())
	}
	return render(request, 'timedisplay_app/index.html', context)