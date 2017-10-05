# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from quiz.models import Quiz , Question

# Register your models here.

admin.site.register(Quiz)
admin.site.register(Question)

