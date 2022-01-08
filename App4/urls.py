from . import views
from django.urls.conf import path 
from App4 import views

urlpatterns =[
    path('',views.index,name='index')
]