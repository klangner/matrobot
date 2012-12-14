# -*- coding: utf-8 -*-
'''
Created on 2012-12-01

@author: Krzysztof Langner
'''
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils.datetime_safe import datetime
from matrobot.project.models import ProjectActivity, TopProject
from matrobot.project.utils import lm
import csv


def index(request):
    name = request.GET.get('name', '')
    if name:
        name = name.strip()
        data = _prepare_chart_data(name)
        if len(data) > 0:
            trend = _calculate_trends(data)
            return render_to_response('project/index.html', {'name':name, 
                                                             'data':data,
                                                             'activity_count':len(data),
                                                             'trend':trend
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
        data.append({'tenure':tenure, 'count':project.push_count, 'committer_count':project.committer_count})
        found_months.add(tenure)
    if len(data) == 0:
        return data
    started = False
    while month < now.month or year < now.year:
        tenure = "%d-%.2d" % (year, month)
        if not tenure in found_months:
            if started:
                data.append({'tenure':tenure, 'count':0, 'committer_count':0})
        else:
            started = True
        month += 1
        if month > 12:
            month = 1
            year += 1
            
    data = sorted(data, key=lambda activity: activity['tenure'])
    return data


def _calculate_trends(activity_infos):
    if len(activity_infos) < 6:
        return 0
    
    data = []
    x = 1
    max_value = 0
    for ai in activity_infos[-6:]:
        data.append({'x': x, 'y': ai['count']})
        max_value = max(ai['count'], max_value)
        x += 1
    scale = max_value/6.0
    if scale > 0:
        for record in data:
            record['y'] = record['y']/scale
    trend = lm(data)
    if trend < -0.2:
        return 1
    elif trend < 0.2:
        return 2
    else:
        return 3 

    
    

def _find_similar_projects(name):
    projects = ProjectActivity.gql("WHERE name>=:1 LIMIT 30", name)
    project_names = set()
    for project in projects:
        if project.name.find(name) >= 0:
            project_names.add(project.name)
    
    return project_names


def download(request):
    name = request.GET.get('name', '')
    if name:
        name = name.strip()
        data = _prepare_chart_data(name)
        if len(data) > 0:
            response = HttpResponse(mimetype='text/csv')
            response['Content-Disposition'] = 'attachment; filename="activity.csv"'
            writer = csv.writer(response)
            writer.writerow(['Repository', 'Push events', 'Committer count'])
            for record in data:
                writer.writerow([record['tenure'], record['count'], record['committer_count']])
            return response
    project_names = _find_similar_projects(name)
    return render_to_response('project/not_found.html', {'name':name, 'project_names':project_names})
    
    
def long_term(request):
    return render_to_response('project/long_term.html')


def top_projects(request):
    projects = TopProject.all()
    return render_to_response('project/top.html', {'projects':projects})