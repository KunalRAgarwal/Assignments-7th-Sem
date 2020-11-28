from django.urls import path
from django.config.urls import url

from . import views

urlpatterns = [
    url('',views.output,name='index'),
]
