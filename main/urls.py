from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
     path('', views.recipe, name='recipe'),
     path('list/', views.recipes_list, name='list'),
     path('detail/', views.recipes_detail, name='detail'),
]