from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView

from .models import Host

from dockerConnect import host_is_available, hostConnection


class IndexView(View):
    def get(self, request):
        return HttpResponse('Index Page')


class ContainersView(TemplateView):
    template_name = 'containers.html'

    def get_context_data(self, **kwargs):
        hosts = Host.objects.all()
        hosts_list = []

        for host in hosts:
            if host_is_available(host.hostname):
                conn = hostConnection(host.hostname, host.conn_type)
                cli = conn.connect()
                hosts_list.append({'id': host.id,
                                   'description': host.description,
                                   'containers': cli.containers()
                                   }
                )
        context = super(ContainersView, self).get_context_data(**kwargs)
        context['hosts_list'] = hosts_list
        return context


class ContainerView(View):
    template_name = 'container.html'

    def get(self, request, *args, **kwargs):
        conn = hostConnection('192.168.33.10:2376', 2)
        cli = conn.connect()
        return render(request, self.template_name, locals())


class HostsView(TemplateView):
    template_name = 'hosts.html'

    def get_context_data(self, **kwargs):
        hosts = Host.objects.all()
        hosts_list = []

        for host in hosts:
            hosts_list.append({'id': host.id,
                                'hostname': host.hostname,
                                'description': host.description,
                                'is_available': host_is_available(host.hostname)
                               }
            )
        context = super(HostsView, self).get_context_data(**kwargs)
        context['hosts_list'] = hosts_list
        return context


class HostView(TemplateView):
    template_name = 'host.html'

    def get_context_data(self, **kwargs):
        host = Host.objects.get(id=kwargs['host_id'])
        conn = hostConnection(host.hostname, host.conn_type)
        cli = conn.connect()
        context = super(HostView, self).get_context_data(**kwargs)
        context['host_model'] = host
        context['host_info'] = cli.info()
        return context


class HostImagesView(TemplateView):
    template_name = 'images.html'

    def get_context_data(self, **kwargs):
        host = Host.objects.get(id=kwargs['host_id'])
        conn = hostConnection(host.hostname, host.conn_type)
        cli = conn.connect()
        context = super(HostImagesView, self).get_context_data(**kwargs)
        context['host_images'] = cli.images()
        context['host_model'] = host
        return context
