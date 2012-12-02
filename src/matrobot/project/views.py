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
            if project.push_count:
                activities.append({'tenure': tenure, 'count': project.push_count})
            else:
                activities.append({'tenure': tenure, 'prediction': project.push_prediction})
        if len(activities) > 0:
            activities = sorted(activities, key=lambda activity: activity['tenure'])
            return render_to_response('project/index.html', {'name':name, 
                                                             'activities':activities,
                                                             'activity_count':len(activities)
                                                             })

    projects = ProjectActivity.gql("WHERE name>=:1 LIMIT 30", name)
    project_names = set()
    for project in projects:
        project_names.add(project.name)
    return render_to_response('project/not_found.html', {'name':name, 'project_names':project_names})
    
    
def long_term(request):
    return render_to_response('project/long_term.html')