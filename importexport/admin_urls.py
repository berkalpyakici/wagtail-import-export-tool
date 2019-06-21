from django.conf.urls import url

from importexport import views


app_name = 'importexport'
urlpatterns = [
    url(r'^import-page/$', views.import_page, name='import-page'),
    url(r'^export-page/$', views.export_page, name='export-page'),
    url(r'^$', views.index, name='index'),
]