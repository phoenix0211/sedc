from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from about import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/', include('about.urls')),
    url(r'^$', RedirectView.as_view(url='about/')),
    url(r'^media/student/(?P<uin>[0-9]+)/$', views.display, name='display'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
