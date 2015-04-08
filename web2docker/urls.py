from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^dockerui/', include('dockerui.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
