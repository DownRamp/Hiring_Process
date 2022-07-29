from django.urls import re_path
from HireApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^job$',views.jobApi),
    re_path(r'^job/([0-9]+)$',views.jobApi),

    re_path(r'^applicant$',views.applicantApi),
    re_path(r'^applicant/([0-9]+)$',views.applicantApi),

    re_path(r'^applicant/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)