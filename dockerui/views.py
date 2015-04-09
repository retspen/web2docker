from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView

from .models import Server

from dkrManager.connect import dkrConnection

class IndexView(View):
    def get(self, request):
        return HttpResponse('Index Page')


class ContainersView(TemplateView):
    template_name = 'containers.html'

    def get_context_data(self, **kwargs):
        servers = Server.objects.all()
        server_list = []

        for server in servers:
            conn = dkrConnection(server.hostname, server.conn_type)
            cli = conn.connect()
            server_list.append({'id': server.id,
                                'description': server.description,
                                'containers': cli.containers()
                                }
            )
        context = super(ContainersView, self).get_context_data(**kwargs)
        context['server_list'] = server_list
        return context


class ContainerView(View):
    template_name = 'container.html'

    def get(self, request, *args, **kwargs):
        conn = dkrConnection('192.168.33.10:2376', 2)
        cli = conn.connect()
        return render(request, self.template_name, locals())


class ServersView(TemplateView):
    template_name = 'servers.html'

    def get_context_data(self, **kwargs):
        servers = Server.objects.all()
        server_list = []

        for server in servers:
            server_list.append({'id': server.id,
                                'hostname': server.hostname,
                                'description': server.description
                                }
            )
        context = super(ServersView, self).get_context_data(**kwargs)
        context['server_list'] = server_list
        return context


class ImagesView(View):
    template_name = 'images.html'

    def get(self, request, *args, **kwargs):
        conn = dkrConnection('192.168.33.10:2376', 2)
        cli = conn.connect()
        print cli.images()
        return render(request, self.template_name, locals())
