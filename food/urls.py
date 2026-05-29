from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('delete/',views.delete_consume,name="consume_delete"),
]
