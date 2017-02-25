from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'scheduler/index.html'

