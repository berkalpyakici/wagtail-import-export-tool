from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class ImportExportAppConfig(AppConfig):
    name = 'importexport'
    label = 'importexport'
    verbose_name = ugettext_lazy("Import/Export Tool")