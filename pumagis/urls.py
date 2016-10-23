from django.conf.urls import url
from rest_framework import routers
from pumagis.views import points_list
from pumagis.views import lines_list

urlpatterns = [
    url(r'^points/$',points_list),
    #url(r'^lines/$',lines_list),
    url(r'^lines/$',lines_list),

]