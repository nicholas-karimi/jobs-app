from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Job 
from .forms import AddJobForm, ApplicationForm

from apps.notification.utilities import create_notification

def job_details(request, job_id):
    job = Job.objects.get(pk=job_id)

    return render(request, 'jobs/job_details.html', {'job': job})


@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False) # commit without saving to db-> specify created by
            job.created_by = request.user 
            job.save()

            return redirect('dashboard')

    else:
        # for -> GET REQ display the form
        form = AddJobForm()

    return render(request, 'jobs/add_job.html', {'form': form})


@login_required
def apply_for_job(request, job_id):
    job = Job.objects.get(pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user 
            application.save()

            create_notification(request, job.created_by, 'application', extra_id=application.id)

            return redirect('dashboard')

    else:
        form = ApplicationForm()

    return render(request, 'jobs/apply_for_job.html', {'form': form, 'job':job})