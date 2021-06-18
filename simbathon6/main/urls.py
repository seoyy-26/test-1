from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('index/', index, name="index"),
    path('left_sidebar/',left_sidebar, name="left_sidebar"),
    path('no_sidebar/', no_sidebar, name="no_sidebar"),
    path('right_sidebar/', right_sidebar, name="right_sidebar"),

]