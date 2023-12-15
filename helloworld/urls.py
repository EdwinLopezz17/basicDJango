
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),
    path('greet/', views.greet, name="greet"),
    path('farewell/', views.farewell, name="farewell"),
    path('adult/<int:age>/', views.adult, name="adult"),
    path('dinamic/<str:name>/', views.dinamic, name="dinamic"),
    path('statics/', views.statics, name="statics"),

]
