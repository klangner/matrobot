# -*- coding: utf-8 -*-
'''
Created on 2012-12-01

@author: Krzysztof Langner
'''

from google.appengine.ext import db

class ProjectActivity(db.Model):
    name = db.StringProperty()
    year = db.IntegerProperty()
    month = db.IntegerProperty()
    push_count = db.IntegerProperty()
    push_prediction = db.IntegerProperty()


class ProjectActivityPrediction(db.Model):
    name = db.StringProperty()
    year = db.IntegerProperty()
    month = db.IntegerProperty()
    push_count = db.IntegerProperty()


class TopProject(db.Model):
    name = db.StringProperty()

#def project_activity_key(name, year, month):
#    return db.Key.from_path("%s-%d-%d", name)
