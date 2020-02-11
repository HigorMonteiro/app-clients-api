from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView
from . import viewset

urlpatterns = {
    url(r'^clients/$', CreateView.as_view(), name="create"),
    url(r'^client/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
    url(r'^clients/$', viewset.client_list, name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
