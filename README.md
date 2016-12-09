User group segmentation
=======================

This plugin requires:
* django-cms: https://github.com/divio/django-cms
* aldryn-segmentation: https://github.com/aldryn/aldryn-segmentation

It adds segmentation by logged in user group.

Installation
------------

1. Install Aldryn Segmentation (not yet in PyPI).
1. Add `'usergroup_segment'` to INSTALLED_APPS in your Django project's
   settings file.
1. `python manage.py migrate usergroup_segment`.
