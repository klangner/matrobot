# -*- coding: utf-8 -*-
'''
Created on 2012-12-01

@author: Krzysztof Langner
'''
from django.shortcuts import render_to_response
from matrobot.project.models import ProjectActivity


def index(request):
    name = request.GET.get('name', '')
    if name:
        name = name.strip()
        activities = []
        projects = ProjectActivity.gql("WHERE name=:1", name)
        for project in projects:
            tenure = "%d-%.2d" % (project.year, project.month)
            activities.append({'tenure': tenure, 'count': project.push_count})
        if len(activities) > 0:
            activities = sorted(activities, key=lambda activity: activity['tenure'])
            return render_to_response('project/index.html', {'name':name, 'activities':activities})
        
    return render_to_response('project/not_found.html', {'name':name})
    
