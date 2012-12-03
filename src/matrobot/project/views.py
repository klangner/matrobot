# -*- coding: utf-8 -*-
'''
Created on 2012-12-01

@author: Krzysztof Langner
'''
from django.shortcuts import render_to_response
from django.utils.datetime_safe import datetime
from matrobot.project.models import ProjectActivity, ProjectActivityPrediction, \
    TopProject


def index(request):
    name = request.GET.get('name', '')
    if name:
        name = name.strip()
        data = _prepare_chart_data(name)
        if len(data) > 0:
            data = _add_forecast(name, data)
            return render_to_response('project/index.html', {'name':name, 
                                                             'data':data,
                                                             'activity_count':len(data)
                                                             })
    project_names = _find_similar_projects(name)
    return render_to_response('project/not_found.html', {'name':name, 'project_names':project_names})
    
    
def _prepare_chart_data(name):
    now = datetime.now()
    year = 2012
    month = 1
    projects = ProjectActivity.gql("WHERE name=:1", name)
    data = []
    found_months = set()
    for project in projects:
        tenure = "%d-%.2d" % (project.year, project.month)
        data.append({'tenure':tenure, 'count':project.push_count})
        found_months.add(tenure)
    if len(data) == 0:
        return data
    while month < now.month or year < now.year:
        tenure = "%d-%.2d" % (year, month)
        if not tenure in found_months:
            data.append({'tenure':tenure, 'count':0})
        month += 1
        if month > 12:
            month = 1
            year += 1
            
    data = sorted(data, key=lambda activity: activity['tenure'])
    
    return data


def _add_forecast(name, data):
    now = datetime.now()
    year = now.year
    month = now.month
    predictions = ProjectActivityPrediction.gql("WHERE name=:1", name)
    for prediction in predictions:
        if prediction.year == year and prediction.month == month:
            last = data[-1]
            last['prediction'] = last['count']
            tenure = "%d-%.2d" % (prediction.year, prediction.month)
            data.append({'tenure':tenure, 'prediction':prediction.push_count})
            break
    return data


def _find_similar_projects(name):
    projects = ProjectActivity.gql("WHERE name>=:1 LIMIT 30", name)
    project_names = set()
    for project in projects:
        if project.name.find(name) >= 0:
            project_names.add(project.name)
    
    return project_names


def long_term(request):
    return render_to_response('project/long_term.html')


def top_projects(request):
    projects = TopProject.all()
    return render_to_response('project/top.html', {'projects':projects})