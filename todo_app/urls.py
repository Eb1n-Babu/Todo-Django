from _pyrepl.commands import delete

from django.urls import path
from django.views.generic import edit

from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('add/',add,name='add'),
    path('delete/<int:task_id>/', delete_task, name='delete'),
    path('toggle/<int:task_id>/', toggle_task, name='toggle'),
]
