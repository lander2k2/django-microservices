import os
from multiprocessing import Process
from subprocess import call

from django.core.management.base import BaseCommand, CommandError
from cluster.models import Service

class TermColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Command(BaseCommand):
    help = 'Runserver on all the services in the cluster'

    def handle(self, *args, **options):
        def run_server(venv, manage_dir, url, settings):
            os.chdir(manage_dir)
            call(['{}/bin/python'.format(venv),
                  '{}/manage.py'.format(manage_dir),
                  'runserver',
                  url,
                  '--settings={}.settings'.format(settings)])

        services = Service.objects.all()
        if not services:
            CommandError('There are no services registered. Add them in your cluster project admin.')
        for service in services:
            p = Process(target=run_server, args=(service.virtual_env,
                                                 service.manage,
                                                 service.url,
                                                 service.name))
            p.start()
            self.stdout.write(
                TermColor.OKGREEN + \
                'Development server started at http://{0} for: {1}'.format(service.url,
                                                                           service.name) + \
               TermColor.ENDC
            )

