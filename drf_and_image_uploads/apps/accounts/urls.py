from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView, TemplateView
from rest_framework.authtoken.views import obtain_auth_token

from . import views
from .views import UserDocUpload

# from .views import UserUpload

urlpatterns = [

    # USER URLS
    path('api-token-auth/', UserDocUpload.as_view()),
    path('jobs/', include('jobs.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

