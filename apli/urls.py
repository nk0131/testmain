from django.urls import path
from . import views

urlpatterns = [
    #path('test', views.test, name='test'),
    path('', views.IndexView.as_view(), name='index'),
]