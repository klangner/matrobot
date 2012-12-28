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
    committer_count = db.IntegerProperty(default=0)


class ProjectDeveloper(db.Model):
    repository = db.StringProperty()
    developer = db.StringProperty()
    event_count = db.IntegerProperty(default=0)


class Repository(db.Model):
    name = db.StringProperty()
    language = db.StringProperty()
    homepage = db.StringProperty()
    created_at = db.StringProperty()


class TopProject(db.Model):
    name = db.StringProperty()

#def project_activity_key(name, year, month):
#    return db.Key.from_path("%s-%d-%d", name)
