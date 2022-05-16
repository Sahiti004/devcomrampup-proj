from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',myapp),
    path('stud/',post_equipm),
    path('upd-stud/<id>',update_equipm),
]