# -*- coding: utf-8 -*-
'''
Created on 2012-12-01

@author: Krzysztof Langner
'''
from django.shortcuts import render_to_response
from django.utils.datetime_safe import datetime
from matrobot.people.models import DeveloperActivity


def index(request):
    name = request.GET.get('name', '')
    if name:
        name = name.strip()
        data = _prepare_chart_data(name)
        if len(data) > 0:
            return render_to_response('people/index.html', {'name':name, 
                                                             'data':data,
                                                             'activity_count':len(data),
                                                             })
    return render_to_response('people/not_found.html', {'name':name})
    
    
def _prepare_chart_data(name):
    now = datetime.now()
    year = 2012
    month = 1
    developers = DeveloperActivity.gql("WHERE name=:1", name)
    data = []
    found_months = set()
    for developer in developers:
        tenure = "%d-%.2d" % (developer.year, developer.month)
        data.append({'tenure':tenure, 'count':developer.activity_count})
        found_months.add(tenure)
    if len(data) == 0:
        return data
    started = False
    while month < now.month or year < now.year:
        tenure = "%d-%.2d" % (year, month)
        if not tenure in found_months:
            if started:
                data.append({'tenure':tenure, 'count':0})
        else:
            started = True
        month += 1
        if month > 12:
            month = 1
            year += 1
            
    data = sorted(data, key=lambda activity: activity['tenure'])
    return data
