from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('pricing', views.pricing, name='pricing'),
    path('jobs', views.job, name='jobs'),
    path('search', views.search, name='search'),
    path('job-search', views.job_search, name='job-search'),
    path('<int:id>/job_detail', views.job_detail, name='detail'),
    # Redirect from paystack
    path('lekki', views.confirm_lekki, name='lekki'),
    path('ikoyi', views.confirm_ikoyi, name='ikoyi'),
    path('eko', views.confirm_eko, name='eko'),
    # Confirmation Page
    path('confirm-lekki', views.lekki_update, name='confirm-lekki'),
    path('confirm-ikoyi', views.ikoyi_update, name='confirm-ikoyi'),
    path('confirm-eko', views.eko_update, name='confirm-eko'), 
  ]

