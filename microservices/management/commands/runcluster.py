import os
from multiprocessing import Process
from subprocess import check_output, Popen

from django.core.management.base import BaseCommand
from django.core.management import call_command

from microservices.models import Service

class TermColor:
    HEADER      = '\033[95m'
    OKBLUE      = '\033[94m'
    OKGREEN     = '\033[92m'
    WARNING     = '\033[93m'
    FAIL        = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'


class Command(BaseCommand):
    help = 'Runserver on all the services in the cluster'

    def handle(self, *args, **options):
        def run_this_server():
            """Start development server for *this* project."""
            call_command('runserver')

        def run_server(venv, manage_dir, url, settings):
            """Start development server for *another* django project."""
            if not venv:
                venv = 'usr'
            os.chdir(manage_dir)
            try:
                check_output(['{}/bin/python'.format(venv),
                      '{}/manage.py'.format(manage_dir),
                      'runserver',
                      url,
                      '--settings={}.settings'.format(settings)])
            except:
                pass

        p = Process(target=run_this_server)
        p.start()

        services = Service.objects.filter(local=True)

        svc_port = 8001
        for service in services:
            service_url = '127.0.0.1:{}'.format(svc_port)
            p = Process(target=run_server, args=(service.virtual_env,
                                                 service.manage,
                                                 service_url,
                                                 service.name))
            p.start()
            self.stdout.write(
                TermColor.OKGREEN + \
                'Development server started at http://{0} for: {1}'.format(service.url,
                                                                           service.name) + \
                TermColor.ENDC
            )
            service.url = service_url
            service.save()
            svc_port += 1

