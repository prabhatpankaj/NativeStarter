# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"