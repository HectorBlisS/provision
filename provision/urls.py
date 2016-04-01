from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Social 
    url('',include('social.apps.django_app.urls',namespace='social')),
    # url(r'^usuario/', include('usuarios.urls')),
    # Archivos
    url(
        regex=r'^media/(?P<path>.*)$',
        view='django.views.static.serve',
        kwargs={'document_root':settings.MEDIA_ROOT}),
    # Fixter
    url(r'^seguimiento/', include('seguimiento.urls')),
    url(r'^',include('main.urls')),
    url(r'^perfil/',include('perfil.urls',
        namespace="perfil")),
]