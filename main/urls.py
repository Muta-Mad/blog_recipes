from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
     path('', views.recipe_create, name='recipe'),
     path('list/', views.recipes_list, name='list'),
     path('<int:pk>', views.recipes_detail, name='detail'),
]