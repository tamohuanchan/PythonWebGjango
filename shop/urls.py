from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:desideorio_id>', views.single_desideorio, name="single_desideorio"),
]