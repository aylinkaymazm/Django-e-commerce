from django.contrib import messages
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormMessage, ContactFormu


# context e yolla burdan render la index.html e yolluyoruz.
from product.models import Product, Category


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:3]
    category = Category.objects.all()

    context = {'setting': setting,
               'category': category,
               'page':'home',
               'sliderdata': sliderdata}
    return render(request,'index.html',context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()

    context = {'setting': setting,
               'category':category}
    return render(request,'hakkimizda.html',context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request,'referanslarimiz.html',context)


def iletisim(request):

    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data= ContactFormMessage()
            data.name= form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip =request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"mesajınız başarı ile gönderilmiştir.Teşekkür ederiz.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category,
               'form':form}
    return render(request,'iletisim.html',context)
