from django.shortcuts import render
from jobs.models import Job


def home(request):
    jobs = Job.objects  # select all the objects from the class Job
    return render(request, 'jobs/home.html', {'jobs': jobs})
