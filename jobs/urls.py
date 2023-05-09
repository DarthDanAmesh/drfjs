from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import RedirectView

from . import views
from .views import UserUpload

urlpatterns = [

    # USER URLS
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    #path('login/', views.user_login, name='login'),

    # ==========================services======================================================================
    # APPLICANT URLS
    # slug is used to generate valid urls
    path('jobs/', views.JobsList.as_view(), name='posted_jobscopy'),
    path('jobs/<slug:slug>/', views.JobsDetail.as_view(), name='posted_jobsdetails'),
    # path('jobs/<int:job_id>/', views.ApplyJobView.as_view(), name='job-details'),
    path('jobs/<int:job_id>/apply/', views.apply_job, name='apply'),
    path('', RedirectView.as_view(pattern_name='jobs-detail', permanent=True)),
    path("jobs/jobseeker/", UserUpload.as_view(), name='index2.html'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)