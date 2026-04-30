
from django.urls import path
from . import views

urlpatterns = [
    path("" , views.all_Apps  , name='all_Apps'),

]
