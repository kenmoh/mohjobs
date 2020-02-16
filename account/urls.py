from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('<int:id>/dashboard', views.freelancer_dashboard, name='dashboard'),
    path('<int:id>/profile', views.user_details, name='profile'),
    path('<int:id>/update', views.create_user_profile, name='update'),
    path('change', views.change_user, name='change'),
    path('<int:id>/delete', views.delete_user, name='delete'),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete')
  ]



   