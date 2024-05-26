from django.contrib import admin
from django.urls import path , include
from myapp import views
urlpatterns = [
    path('' , views.index , name = "index"),
    path('update/<id>' , views.update  , name = "update"),
    path('delete/<id>' , views.delete , name = "delete")
   
]
