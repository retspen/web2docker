from django.conf.urls import url

from views import IndexView, ConteinersView, ContainerView, ImagesView

urlpatterns = [
    # ex: /polls/
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^containers/$', ConteinersView.as_view(), name='containers'),
    url(r'^container/(?P<container_id>[0-9a-f]+)/$', ContainerView.as_view(), name='container'),
    url(r'^images/$', ImagesView.as_view(), name='images'),
]
