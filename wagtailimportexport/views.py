from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.translation import ungettext, ugettext_lazy as _


def index(request):
    """
    View for main menu of the Import/Export tool. Provides a list
    of features.
    """
    return render(request, 'wagtailimportexport/index.html')

def import_page(request):
    """
    View for the import page.
    """
    return render(request, 'wagtailimportexport/import-page.html')

def export_page(request):
    """
    View for the export page.
    """
    return render(request, 'wagtailimportexport/export-page.html')