django-sluggee
==============

Django-package to slugify Russian easily.

.. image:: https://api.travis-ci.org/koorgoo/django-sluggee.png

Getting Started
---------------

Installation
^^^^^^^^^^^^
::

    pip install django-sluggee
::

Usage
^^^^^
::

    from django.db import models
    from sluggee.utils import slugify

    class Entry(models.Model):
        title = models.CharField(max_length=100)
        body = models.TextField()
        slug = models.SlugField()

        def __unicode__(self):
            return self.title

        def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.title)[:50]

            return super(Entry, self).save(*args, **kwargs)
::
