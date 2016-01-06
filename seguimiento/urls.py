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

    url(r'^login/$',
        views.Login.as_view(),
        name='_login'),
    
    url(r'^tfacil$',
        views.TerrenoFacilForm.as_view(),
        name='_tfacil'),

	]