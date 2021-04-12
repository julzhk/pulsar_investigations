import os
import sys
from django.conf import settings
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from datetime import datetime
import pulsar
import random as rd
import time as t
import json
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import Template, Context
from django.views.decorators.csrf import csrf_exempt


class NameForm(forms.Form):
    your_msg = forms.CharField(label='Your message', max_length=100)


def index(request):
    message = ''
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            message = 'submitted'
            send_message(form.cleaned_data.get('your_msg'))
    else:
        form = NameForm()

    template = Template('''
        {{message}} 
        <form action="." method="post">
        {{ form }}
        <input type="submit" value="OK">
        </form>
        ''')
    context = Context(dict(message=message, form=form))
    rendered: str = template.render(context)
    return HttpResponse(rendered)


def send_message(msg):
    client = pulsar.Client('pulsar://pulsar:6650')
    producer = client.create_producer('my-topic')
    producer.send(
        json.dumps(
            {
                'time': f'{datetime.now()}',
                'message': msg
            }
        ).encode('utf-8')
    )
    client.close()


urlpatterns = (
    url(r'^$', csrf_exempt(index)),
)
BASE_DIR = os.path.dirname(__file__)
if __name__ == "__main__":
    settings.configure(
        DEBUG=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'None',
            }
        },
        SECRET_KEY=os.environ.get('SECRET_KEY', '2342tfdgfdgdfgDSFDSFsdgsdf2234252'),
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS='*',
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ),
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        }]
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
