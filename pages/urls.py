from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('terms', views.terms, name='terms'),
    path('policy', views.policy, name='policy'),
    path('contact', views.contact, name='contact'),
    path('pricing', views.pricing, name='pricing'),
    path('jobs', views.job, name='jobs'),
    path('search', views.search, name='search'),
    path('job-search', views.job_search, name='job-search'),
    path('<int:id>/job_detail', views.job_detail, name='detail'),
    # Redirect from paystack
    path('silver', views.confirm_silver, name='silver'),
    path('gold', views.confirm_gold, name='gold'),
    path('platinum', views.confirm_platinum, name='platinum'),
    # Confirmation Page
    path('confirm-silver', views.silver_update, name='confirm-silver'),
    path('confirm-gold', views.gold_update, name='confirm-gold'),
    path('confirm-platinum', views.platinum_update, name='confirm-platinum'), 
  ]

