import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wagtail-import-export-tool",
    version="0.9.2",
    author="Berk Alp Yakici",
    author_email="contact@berkalpyakici.com",
    description="Import/Export tool for Wagtail CMS (built on top of Django), that supports pages, images, documents, and snippets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/berkalpyakici/wagtail-import-export-tool",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Operating System :: OS Independent",
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
)