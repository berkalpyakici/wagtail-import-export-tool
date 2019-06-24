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

## Known Limitations
Page models should be consistent across both source and destination environments. Otherwise, importing may fail due to mismatching fields.

## Credits
This project is based on [torchbox/wagtail-import-export](https://github.com/torchbox/wagtail-import-export). As they use the same Django application name, both cannot run.