from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^inicio/$', 
    views.SeguiStatus.as_view(),
    name='_inicio'), 

    # url(r'^$',
    # views.SeguiIndex.as_view(),
    # name='_index'), 

    url(r'^gracias/$',
    views.RecibeGracias.as_view(),
    name='_recibe'),

    url(r'^inicio/(?P<id>\d+)',
    views.Revisar.as_view(),
    name='_revisar'),

    # Lista filtrada por revisados
    url(r'^inicio/filtro/(?P<filtro>\w+)/$',
        views.SeguiStatus.as_view(),
        name='_inicio_filtro'),

    url(r'^login/$',
        views.Login.as_view(),
        name='_login'),
    
    url(r'^tfacil$',
        views.TerrenoFacilForm.as_view(),
        name='_tfacil'),

    url(r'^thanks/$',
        views.TakeForm.as_view(),
        name='_daform'),

    url(r'^borra/(?P<id>\d+)',
        views.Borra.as_view(),
        name='_borra'),

    # Guardar comentario del contacto
    url(r'^revisado/(?P<id>\d+)',
        views.Revisado.as_view(),
        name='_add-coment'),

    

	]