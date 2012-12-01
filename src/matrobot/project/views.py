# -*- coding: utf-8 -*-
'''
Created on 2012-12-01

@author: Krzysztof Langner
'''
from django.shortcuts import render_to_response
from matrobot.project.models import ProjectActivity


def index(request):
    name = request.GET.get('name', '')
    activity = ProjectActivity.objects.all().filter(name=name)
    if activity:
        pass
    else:
        return render_to_response('project/not_found.html', {'name':name})
    
    return render_to_response('project/index.html', {'name':name})
