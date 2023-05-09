from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.admin import TokenAdmin

from jobs.models import Job
from .models import User

TokenAdmin.raw_id_fields = ['user']


class UserAdmin(UserAdminBase):
    readonly_fields = ["username"]

    fieldsets = list(UserAdminBase.fieldsets) + [
        (_("Extra"), {"fields": ["middle_name", "first_two_names", "id_number",
                                 "email", "cover", "resume", "contact", "location"]})
    ]


class PostJobAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'job_type', 'staff', 'date_posted')
    list_filter = ("staff", "qualifications_req",)
    readonly_fields = ["slug", ]
    search_fields = ['title', 'content', 'experience_level', 'job_type']


admin.site.register(Job, PostJobAdmin)
admin.site.register(User)
