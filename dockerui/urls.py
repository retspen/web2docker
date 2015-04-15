from django.conf.urls import url

from views import IndexView, ContainersView, ContainerView, HostImagesView, HostsView, HostInfoView

urlpatterns = [
    # ex: /polls/
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^containers/$', ContainersView.as_view(), name='containers'),
    url(r'^container/(?P<host_id>[0-9]+)/(?P<container_id>[0-9a-f]+)/$', ContainerView.as_view(), name='container'),
    url(r'^servers/$', HostsView.as_view(), name='hosts'),
    url(r'^server/(?P<host_id>[0-9]+)/$', HostInfoView.as_view(), name='host'),
    url(r'^images/(?P<host_id>[0-9]+)/$', HostImagesView.as_view(), name='images'),
]
