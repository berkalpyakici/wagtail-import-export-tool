from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ImportExportAppConfig(AppConfig):
    name = 'importexport'
    label = 'importexport'
    verbose_name = _("Import/Export Tool")