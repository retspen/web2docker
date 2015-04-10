from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView

from .models import Server

from dkrManager.connect import dkrConnection
from dkrManager.utils import host_is_available


class IndexView(View):
    def get(self, request):
        return HttpResponse('Index Page')


class ContainersView(TemplateView):
    template_name = 'containers.html'

    def get_context_data(self, **kwargs):
        servers = Server.objects.all()
        server_list = []

        for server in servers:
            if host_is_available(server.hostname):
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
                                'description': server.description,
                                'is_available': host_is_available(server.hostname)
                                }
            )
        context = super(ServersView, self).get_context_data(**kwargs)
        context['server_list'] = server_list
        return context


class ServerView(TemplateView):
    template_name = 'server.html'

    def get_context_data(self, **kwargs):
        server = Server.objects.get(id=kwargs['server_id'])
        conn = dkrConnection(server.hostname, server.conn_type)
        cli = conn.connect()
        context = super(ServerView, self).get_context_data(**kwargs)
        context['server_model'] = server
        context['server_info'] = cli.info()
        return context


class ImagesView(View):
    template_name = 'images.html'

    def get(self, request, *args, **kwargs):
        conn = dkrConnection('192.168.33.10:2376', 2)
        cli = conn.connect()
        print cli.images()
        return render(request, self.template_name, locals())
