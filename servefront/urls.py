from django.contrib import admin
from django.urls import path,include

from django.views.generic import TemplateView

app_name='servefront'
urlpatterns=[
    path('',TemplateView.as_view(template_name='servefront/home.html'),name='home-url'),

]