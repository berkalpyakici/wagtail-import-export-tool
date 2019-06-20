from django.conf.urls import url

from importexport import views


app_name = 'importexport'
urlpatterns = [
    url(r'^import/$', views.imports, name='import'),
    url(r'^export/$', views.exports, name='export'),
    url(r'^$', views.index, name='index'),
]