from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
     path('', views.recipe, name='recipe'),
     path('recipes_list/', views.recipes_list, name='recipes_list'),
]