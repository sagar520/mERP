from django.conf.urls import include, url
from .views import *
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()

# router.register(r'test/$' , UserCountView.as_view() )

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'$' , mailBoxView )
]

urlpatterns = format_suffix_patterns(urlpatterns)