from django.contrib import admin
from django.conf.urls import url,include
from .views import home,about,contact
from blog.views import postDetay,postDetay2,postDetay3,postDetay4,GonderilerGezi,GonderilerFilm,GonderilerDizi,GonderilerHayat


#views.index
urlpatterns = [
    url(r'^home/$', view=home, name='home'),
    url(r'^about/$', view=about, name='about'),
    url(r'^contact/$', view=contact, name='contact'),
    
    url(r'^GonderilerGezi/$', view=GonderilerGezi, name='GonderilerGezi'),
    url(r'^GonderilerGezi/postDetay/(?P<slug>[-\w]+)/$',postDetay,name='post-detay'),

    url(r'^GonderilerDizi/$', view=GonderilerDizi, name='GonderilerDizi'),
    url(r'^GonderilerDizi/postDetay2/(?P<slug>[-\w]+)/$',postDetay2,name='post-detay2'),
    
    url(r'^GonderilerFilm/$', view=GonderilerFilm, name='GonderilerFilm'),
    url(r'^GonderilerFilm/postDetay3/(?P<slug>[-\w]+)/$',postDetay3,name='post-detay3'),

    url(r'^GonderilerHayat/$', view=GonderilerHayat, name='GonderilerHayat'),
    url(r'^GonderilerHayat/postDetay4/(?P<slug>[-\w]+)/$',postDetay4,name='post-detay4'),
]
