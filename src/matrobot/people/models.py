# -*- coding: utf-8 -*-
'''
Created on 2012-12-01

@author: Krzysztof Langner
'''

from google.appengine.ext import db

class CommitterActivity(db.Model):
    name = db.StringProperty()
    year = db.IntegerProperty()
    month = db.IntegerProperty()
    commit_count = db.IntegerProperty(default=0)
