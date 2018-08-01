from django.conf.urls import url
from . import views

app_name = 'about'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about.html$', views.about, name='about'),
    url(r'^login.html$', views.login, name='login'),
    url(r'^upload.html$', views.upload, name='upload'),
    url(r'^qrcode.html$', views.qrcode, name='qrcode'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^forgot.html$', views.forgot, name='forgot'),
    url(r'^fgerr.html$', views.fgerr, name='frerr'),
    url(r'^cng_pwd.html$', views.change, name='change'),
    #url(r'^display.html$', views.display, name='display'),
]