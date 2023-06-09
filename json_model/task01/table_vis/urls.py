from django.urls import path

from  .import views as view

urlpatterns = [
    path('tablev', view.tablev, name='tablev'),
    path('', view.tableview, name='tableview'),
]