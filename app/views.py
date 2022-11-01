
from lib2to3.pgen2.token import tok_name
from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
def display_topic(request):
    topics=Topic.objects.all()

    d={'ts':topics}
    return render(request,'display_topic.html',d)



def display_webpages(request):
    webpages=Webpages.objects.all()
    webpages=Webpages.objects.filter(topic_name='Football')
    #webpages=Webpages.objects.exclude(topic_name='Foot Ball')
    #webpages=Webpages.objects.all()[0:2:]
    #webpages=Webpages.objects.all()[-3]
    webpages=Webpages.objects.all().order_by('name')
    webpages=Webpages.objects.all().order_by('-name')
    webpages=Webpages.objects.all().order_by(Length('name'))
    webpages=Webpages.objects.all().order_by(Length('name').desc())
    webpages=Webpages.objects.filter(name__startswith='s')
    webpages=Webpages.objects.filter(name__endswith='i')
    webpages=Webpages.objects.filter(name__contains='s')
    webpages=Webpages.objects.filter(name__in=('Mugesh','sasi'))
    webpages=Webpages.objects.filter(name__regex='\w{6}')
    webpages=Webpages.objects.filter(Q(name='Mugesh') | Q(name='sasi'))

    d={'ws':webpages}
    return render(request,'display_webpages.html',d)

def display_Accessrecord(request):
    access=Accessrecords.objects.all()
    d={'ac':access}
    return render(request,'display_Accessrecord.html',d)