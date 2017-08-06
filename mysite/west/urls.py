from django.conf.urls import  include, url
from west.views import first_page

urlpatterns = [
    url(r"^$",first_page),
]

