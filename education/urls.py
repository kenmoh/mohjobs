from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_education, name='education'),
    path('<int:id>/edit', views.edit_education, name='edit_education'),
    path('<int:id>/delete', views.delete_edu, name='delete-edu'),
  ]