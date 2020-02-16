from django.urls import path

from . import views


urlpatterns = [
    path('<int:id>/update/profile', views.employer_profile, name='company_profile'),
    path('<int:id>/dashboard', views.employer_dashboard, name='employer-dashboard'),
    path('add/post', views.post, name='post'),
    path('<int:id>/job/delete', views.delete_job, name='delete-job'),
    path('<int:id>/job/edit', views.edit_post, name='edit'),
  ]
