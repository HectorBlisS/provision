from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^inicio/$', 
    views.SeguiStatus.as_view(),
    name='_inicio'), 

    url(r'^$',
    views.SeguiIndex.as_view(),
    name='_index'), 

    url(r'^gracias/$',
    views.RecibeGracias.as_view(),
    name='_recibe'),

    url(r'^inicio/(?P<id>\d+)',
    views.Revisar.as_view(),
    name='_revisar'),

	]