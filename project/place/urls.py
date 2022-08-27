from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main),
    re_path(r'^canvas1/', Canvas1.as_view(), name='canvas1'),
]
