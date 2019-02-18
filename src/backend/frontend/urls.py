from django.contrib import admin
from django.urls import path

from frontend import views


urlpatterns = [
    path('tools/url-to-domain/', views.uri_to_domain_view, name="uri_to_domain_view"),
]
