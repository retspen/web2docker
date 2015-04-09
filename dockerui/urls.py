from django.conf.urls import url

from views import IndexView, ContainersView, ContainerView, ImagesView, ServersView

urlpatterns = [
    # ex: /polls/
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^containers/$', ContainersView.as_view(), name='containers'),
    url(r'^container/(?P<container_id>[0-9a-f]+)/$', ContainerView.as_view(), name='container'),
    url(r'^servers/$', ServersView.as_view(), name='servers'),
    url(r'^images/$', ImagesView.as_view(), name='images'),
]
