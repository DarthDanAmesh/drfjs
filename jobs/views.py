from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_and_image_uploads.apps.accounts.serializers import UserUploadSerializer
from jobs.models import Job, Application


# Create your views here.

def contact(request):
    context = {
        'contact': "active",
    }
    return render(request, 'jobseeker/contact.html', context)


# SERVICES
def services(request):
    context = {
        'services': "active",
    }
    return render(request, 'jobseeker/services.html', context)


def home(request):
    context = {
        'home': "active",
    }
    return render(request, 'jobseeker/home.html', context)


# ----------------------------------------------------------------------------------------------
# JOB _DETAILS
def job_details(request, job_id):
    user = request.user
    job = Job.objects.get(id=job_id)
    already_applied = False
    # compare the skills in the job with those all the user
    relevant_jobs = list()

    context = {'job': job, 'relevant_jobs': relevant_jobs}


class JobsList(generic.ListView):
    queryset = Job.objects.order_by('-date_posted')
    # used on the html side for-loop
    context_object_name = "job_list"
    paginate_by = 3
    template_name = 'jobseeker/all_jobs.html'


class JobsDetail(generic.DetailView):
    model = Job
    context_object_name = "job_details"
    template_name = 'jobseeker/posted_jobsdetails.html'


def apply_job(request, slug):
    user = request.user
    job = get_object_or_404(Job, slug=slug)
    applied, created = Application.objects.get_or_create(job=job, user=user)
    applicant, creation = User.objects.get_or_create(
        job=job, applicant=user)
    return HttpResponseRedirect('/job/{}'.format(job.slug))


"""class ApplyJobView(View):
    form_class = JobApplicationForm
    # initial = {"key": "value"}
    template_name = "applicant/apply.html"

    def post(self, request, *args, **kwargs):
        if not self.form_class(request.POST):
            #form = JobApplicationForm()
            job = Job.objects.get(id=kwargs['job_id'])
            context = {
                #'form': form,
                'job': job
            }
            return render(request, self.template_name, context)

        return redirect('posted-jobs')
    # add functions for users logged in
"""


class UserUpload(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserUploadSerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
