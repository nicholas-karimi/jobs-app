from django.urls import path, include 

from .views import dashboard, view_application, view_job

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('application/<int:app_id>/', view_application, name='view_application'),
    path('job/<int:job_id>/', view_job, name='view_job_detail'),
]