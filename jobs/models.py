# Create your models here.
from autoslug import AutoSlugField
from django.db import models
from django.db.models import CASCADE, UniqueConstraint
from django.utils import timezone

from drf_and_image_uploads.apps.accounts.models import COUNTIES_LIST
from drf_and_image_uploads.apps.accounts.serializers import User

JOB_TYPES = (
    ('Full Time', 'Full Time'),
    ('Contract', 'Contract Time'),
    ('Internship', 'Internship'),
    ('Industrial Attachment', 'Industrial Attachment'),
)

EXPERIENCE_LEVEL = [
    ('ENTRY-LEVEL', 'ENTRY-LEVEL'),
    ('INTERMEDIATE-LEVEL', 'INTERMEDIATE-LEVEL'),
    ('MID-LEVEL', 'MID-LEVEL'),
    ('SENIOR OR EXECUTIVE-LEVEL', 'SENIOR OR EXECUTIVE-LEVEL'),
]


class Job(models.Model):
    company = models.CharField(max_length=100, default="Kenya Bureau of Standards - KEBS")
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50, choices=JOB_TYPES, default='Full Time', null=True)
    description = models.TextField()
    qualifications_req = models.CharField(max_length=1000, null=True, editable=True)
    experience_level = models.CharField(max_length=30, choices=EXPERIENCE_LEVEL, default='MID-LEVEL')
    remuneration = models.CharField(max_length=50, default="N/A")
    location = models.CharField(max_length=20, choices=COUNTIES_LIST, default='Nairobi')
    date_posted = models.DateTimeField(default=timezone.now)
    deadline = models.DateField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    slug = AutoSlugField(populate_from='title', editable=False, always_update=True)
    staff = models.ForeignKey(User, default="", on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=CASCADE)
    applicant = models.ForeignKey(User, on_delete=CASCADE)
    date_applied = models.DateTimeField()

    class Meta:
        constraints = [
            UniqueConstraint(fields=['job', 'applicant'], name='unique_applicant_job_match')
        ]


class Candidates(models.Model):
    job = models.ForeignKey(Job, related_name='candidates', on_delete=models.CASCADE)
    candidate = models.ForeignKey(User, related_name='applied', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.candidate


class AppliedJobs(models.Model):
    job = models.ForeignKey(Job, related_name='applied_job', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='applied_user', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.title
