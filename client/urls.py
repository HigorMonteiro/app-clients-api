from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import viewset

urlpatterns = {
    url(r'^clients/$', viewset.client_list, name="create"),
    url(r'^clients/(?P<pk>[0-9]+)$', viewset.client_detail, name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
