from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Azienda
from .models import File
from .forms import FileForm
from .forms import DocumentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.core.servers.basehttp import FileWrapper
from django.shortcuts import render, get_object_or_404
import os, tempfile, zipfile
import mimetypes


# Create your views here.

def post_list2(request):
    posts = Azienda.objects.filter(ragsoc__lte='New Safety Work').order_by('ragsoc')
    send_mail('Ciao', 'Ciao ciao', 'raffaele.lionetti@tianetworks.it', 'raffaele.lionetti@tianetworks.it', fail_silently=False)
    return render(request, 'arearis/post_list.html', {'posts': posts})

def post_list(request):
    posts = File.objects.filter(utente__lte=request.user).order_by('utente')
    send_mail('Ciao', 'Ciao ciao', 'ra.lionetti@gmail.com', [request.user.email], fail_silently=False)
    return render(request, 'arearis/post_list.html', {'posts': posts})

def add_file(request):
    if request.method == "POST":
        form = FileForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.utente = request.user
            post.created_date = timezone.now()
            post.save()
            #return redirect('post_detail', pk=post.pk)
    else:
        form = FileForm()
    return render(request, 'arearis/fileadd.html', {'form': form})

def list(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILE)
        if form.is_valid():
            handle_uploaded_file(request.FILES['upload'])
            return HttResponseRedirect('/success/url/')
            #newdoc = File(upload.POST, request.FILE['upload'])
            #newdoc.save()
    else:
        form = FileForm()
    return render(request, 'arearis/fileadd.html', {'form': form})

@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.utente = request.user
            azie = Azienda.objects.filter(utente = request.user)
            #form.azienda = azie[0].ragsoc#File.objects.filter(azienda = azie) #File.objects.filter(azienda = Azienda.objects.filter(utente = request.user))
            form.created_date = timezone.now()
            form.save()
            send_mail('Ciao', 'Ciao ciao', 'ra.lionetti@gmail.com', ['raffaele.lionetti@tianetworks.it'], fail_silently=False)
            #return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'arearis/model_form_upload.html', {
        'form': form
    })


def download1(request, path):
    filename = 'upload/M73017_20170000_CR.pdf'
    wrapper = FileWrapper(filename)
    response = HttpResponse(wrapper,content_type=mimetypes.guess_type(filename)[0])
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = "attachment; filename=" + filename
    return response

def download(request, pk):
    percorso = File.objects.filter(pk=pk)
    perc = str(percorso[0].upload)
#'upload/M73017_20170000_CR_V8n7RGz.pdf'
    fp = open(perc, 'rb')
    response = HttpResponse(fp.read())
    fp.close()
    type, encoding = mimetypes.guess_type(perc)
    if type is None:
        type = 'application/octet-stream'
    response['Content-Type'] = type
    response['Content-Length'] = str(os.stat(perc).st_size)
    if encoding is not None:
        response['Content-Encoding'] = encoding


    return response

#def download(request):
#    fp = open('upload/gestionerischi.tar.gz', 'rb')
#    response = HttpResponse(fp.read())
#    fp.close()
#    type, encoding = mimetypes.guess_type('gestionerischi.tar.gz')
#    if type is None:
#        type = 'application/octet-stream'
#    response['Content-Type'] = type
#    response['Content-Length'] = str(os.stat('upload/gestionerischi.tar.gz').st_size)
#    if encoding is not None:
#        response['Content-Encoding'] = encoding
#
#
#    return response

def post_detail(request, pk):
        post = get_object_or_404(File, pk=pk)
        return render(request, 'arearis/post_list.html', {'post': post})


