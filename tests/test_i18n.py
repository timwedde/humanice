#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for filesize humanizing."""

import os
import datetime
import humanice as h
from unittest.mock import patch
import gettext as gettext_module
from .base import HumaniceTestCase


class FilesizeTestCase(HumaniceTestCase):

    def test_load_localizations(self):
        locale_dir = h.i18n._DEFAULT_LOCALE_PATH
        locales = [item for item in os.listdir(locale_dir)
                   if os.path.isdir(os.path.join(locale_dir, item))]
        for locale in locales:
            with patch("humanice.i18n._CURRENT") as mocked:
                mocked.return_value = "locale"
                result = h.naturaltime(datetime.timedelta(seconds=3))
                self.assertEqual(result, "3 seconds ago")
                h.i18n.activate(locale)
                result = h.naturaltime(datetime.timedelta(seconds=3))
                h.i18n.deactivate()
                result = h.naturaltime(datetime.timedelta(seconds=3))
                self.assertEqual(result, "3 seconds ago")

    def test_load_null_translation(self):
        t = h.i18n.activate(None)
        self.assertTrue(isinstance(t, gettext_module.NullTranslations))

    def test_load_translation_with_path(self):
        t = h.i18n.activate(None, path=h.i18n._DEFAULT_LOCALE_PATH)
        self.assertTrue(isinstance(t, gettext_module.NullTranslations))
