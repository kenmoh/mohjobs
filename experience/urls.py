from django.urls import path
from . import views

urlpatterns = [ 
    path('add', views.add_experience, name='experience'),
    path('<int:id>/edit', views.edit_experience, name='edit_experience'),
    path('<int:id>/delete', views.delete_exp, name='delete-exp'),
  ]