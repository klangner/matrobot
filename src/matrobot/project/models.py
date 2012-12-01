# -*- coding: utf-8 -*-
'''
Created on 2012-12-01

@author: Krzysztof Langner
'''

from django.db import models


class ProjectActivity(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    month = models.IntegerField()
    push_count = models.IntegerField()
    
    def __str__(self):
        return self.name
