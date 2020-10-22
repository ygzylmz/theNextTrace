from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import BlogGezi,BlogDizi,BlogFilm,BlogHayat,ImagesBlogGezi,ImagesBlogFilm,ImagesBlogDizi,ImagesBlogHayat
from django.forms import modelformset_factory

def GonderilerGezi(request):
    posts = BlogGezi.objects.all()
    context = {'posts': posts}
    return render(request,'yazilar.html',context)

def GonderilerDizi(request):
    posts = BlogDizi.objects.all()
    context = {'posts': posts}
    return render(request,'yazilar2.html',context)

def GonderilerFilm(request):
    posts = BlogFilm.objects.all()
    context = {'posts': posts}
    return render(request,'yazilar3.html',context)

def GonderilerHayat(request):
    posts = BlogHayat.objects.all()
    context = {'posts': posts}
    return render(request,'yazilar4.html',context)

def postDetay(request,slug):
    blogGezi = get_object_or_404(BlogGezi,slug=slug)
    photos = ImagesBlogGezi.objects.filter(blog=blogGezi)
    print("DenemeBlog:", blogGezi)
    print("DenemeOnur:", photos)
    return render(request,'postDetay.html',context={'blog':blogGezi,'photos':photos})

def postDetay2(request,slug):
    blogDizi = get_object_or_404(BlogDizi,slug=slug)
    photos = ImagesBlogDizi.objects.filter(blog=blogDizi)
    print("DenemeBlog:", blogDizi)
    print("DenemeOnur:", photos)
    return render(request,'postDetay2.html',context={'blog':blogDizi,'photos':photos})

def postDetay3(request,slug):
    blogFilm = get_object_or_404(BlogFilm,slug=slug)
    photos = ImagesBlogFilm.objects.filter(blog=blogFilm)
    print("DenemeOnurFilm:", photos)
    return render(request,'postDetay3.html',context={'blog':blogFilm,'photos':photos})

def postDetay4(request,slug):
    blogHayat = get_object_or_404(BlogHayat,slug=slug)
    photos = ImagesBlogHayat.objects.filter(blog=blogHayat)
    print("DenemeOnurFilm:", photos)
    return render(request,'postDetay4.html',context={'blog':blogHayat,'photos':photos})


