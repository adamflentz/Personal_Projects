# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class home(TemplateView):
    def get(self, request):
        return render(request, 'home.html', locals())
