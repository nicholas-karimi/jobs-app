from django.urls import path, include 

from .views import job_details, add_job, apply_for_job

urlpatterns = [
    path('add/', add_job, name='new_job'),
    path('<int:job_id>/', job_details, name='job_details'),
    path('<int:job_id>/apply_for_job', apply_for_job, name='apply_for_job'),
]