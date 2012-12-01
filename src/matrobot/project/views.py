# -*- coding: utf-8 -*-
'''
Created on 2012-12-01

@author: Krzysztof Langner
'''
from django.shortcuts import render_to_response
from matrobot.project.models import ProjectActivity, project_activity_key


def index(request):
    name = request.GET.get('name', '')
    if name:
        projects = ProjectActivity.gql("WHERE ANCESTOR IS :1 AND name=:2",
                                   project_activity_key(name),
                                   name)
        if projects.count(1) > 0:
            return render_to_response('project/index.html', {'name':name})
        
    return render_to_response('project/not_found.html', {'name':name})
    
