# Wagtail Import/Export Tool
Import/Export tool for Wagtail CMS (built on top of Django), that supports pages, images, documents, and snippets.

## Installation
Install `wagtail-import-export-tool` using PIP.
```
pip install wagtail-import-export-tool
```

Add `wagtailimportexport` to your Django project settings.
```
INSTALLED_APPS = [
    ...
    'wagtailimportexport',
    ...
]
```

## Config
App settings can be found in `wagtailimportexport/config.py` file.

## Known Limitations
* Page models should be consistent across both source and destination environments. Otherwise, importing may fail due to mismatching fields.
* Exporting snippets is not implemented yet.

## Credits
This project is based on [torchbox/wagtail-import-export](https://github.com/torchbox/wagtail-import-export). Because they use the same Django application name, both cannot be used on the same project at the same time.