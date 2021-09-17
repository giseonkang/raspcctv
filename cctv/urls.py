from django.contrib import admin
from django.urls import path
from cctv.views import *
urlpatterns =[
    path('',CamView.as_view),
    path('snapshot/', snapshot, name='snapshot'),
    path('stream/',cctv_stream , name='stream'),
]