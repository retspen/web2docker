from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from dkrManager.connect import dkrConnection


class IndexView(View):
    def get(self, request):
        return HttpResponse('Index Page')


class ConteinersView(View):
    template_name = 'containers.html'

    def get(self, request):
        conn = dkrConnection('192.168.33.10:2376', 2)
        cli = conn.connect()
        return render(request, self.template_name, locals())


class ContainerView(View):
    template_name = 'container.html'

    def get(self, request, *args, **kwargs):
        conn = dkrConnection('192.168.33.10:2376', 2)
        cli = conn.connect()
        return render(request, self.template_name, locals())


class ImagesView(View):
    template_name = 'images.html'

    def get(self, request, *args, **kwargs):
        conn = dkrConnection('192.168.33.10:2376', 2)
        cli = conn.connect()
        print cli.images()
        return render(request, self.template_name, locals())
