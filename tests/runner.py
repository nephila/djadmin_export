#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2011-2013 Raphaël Barrois
# This code is distributed under the two-clause BSD license.

from __future__ import unicode_literals

import sys

import django
from django.conf import settings
from django.test.runner import DiscoverRunner as DjangoTestSuiteRunner


if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'tests',
            'djadmin_export',
        ],
        MIDDLEWARE_CLASSES=[],
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
        }],
    )

django.setup()

default_test_args = 'tests.utils'


def runtests(*test_args):
    if not test_args:
        test_args = [default_test_args]
    runner = DjangoTestSuiteRunner(failfast=False)
    failures = runner.run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
