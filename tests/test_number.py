#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Number tests."""

from humanice import number
from .base import HumaniceTestCase


class NumberTestCase(HumaniceTestCase):

    def test_ordinal(self):
        test_list = ('1', '2', '3', '4', '11', '12', '13', '101', '102', '103',
                     '111', 'something else', None)
        result_list = ('1st', '2nd', '3rd', '4th', '11th', '12th', '13th',
                       '101st', '102nd', '103rd', '111th', 'something else', None)
        self.assertManyResults(number.ordinal, test_list, result_list)

    def test_intcomma(self):
        test_list = (100, 1000, 10123, 10311, 1000000, 1234567.25, '100',
                     '1000', '10123', '10311', '1000000', '1234567.1234567', None)
        result_list = ('100', '1,000', '10,123', '10,311', '1,000,000',
                       '1,234,567.25', '100', '1,000', '10,123', '10,311',
                       '1,000,000', '1,234,567.1234567', None)
        self.assertManyResults(number.intcomma, test_list, result_list)

    def test_intcomma_ndigits(self):
        test_list = ((14308.40, None), (14308.40, 1), (14308.40, 2),
                     (14308.40, 3), (1234.5454545,), (1234.5454545, None),
                     (1234.5454545, 1), (1234.5454545, 2), (1234.5454545, 3),
                     (1234.5454545, 10))
        result_list = ("14,308.4", "14,308.4", "14,308.40",
                       "14,308.400", "1,234.5454545", "1,234.5454545",
                       "1,234.5", "1,234.55", "1,234.545", "1,234.5454545000")
        self.assertManyResults(number.intcomma, test_list, result_list)

    def test_intword(self):
        # make sure that powers & human_powers have the same number of items
        self.assertEqual(len(number.powers), len(number.human_powers))
        # test the result of intword
        test_list = ('100', '1000000', '1200000', '1290000', '999999999',
                     '1000000000', '2000000000', '6000000000000',
                     '1300000000000000', '3500000000000000000000',
                     '8100000000000000000000000000000000', None,
                     ('1230000', '%0.2f'), 10**101)
        result_list = ('100', '1.0 million', '1.2 million', '1.3 million',
                       '1.0 billion', '1.0 billion', '2.0 billion',
                       '6.0 trillion', '1.3 quadrillion', '3.5 sextillion',
                       '8.1 decillion', None, '1.23 million', '1' + '0' * 101)
        self.assertManyResults(number.intword, test_list, result_list)

    def test_apnumber(self):
        test_list = (-1, 0, 1, 2, 4, 5, 9, 10, '7', None)
        result_list = ("-1", "zero", 'one', 'two', 'four', 'five', 'nine', '10',
                       'seven', None)
        self.assertManyResults(number.apnumber, test_list, result_list)

    def test_fractional(self):
        test_list = (1, 2.0, (4.0 / 3.0), (5.0 / 6.0), '7', '8.9', 'ten', None)
        result_list = ('1', '2', '1 1/3', '5/6', '7', '8 9/10', 'ten', None)
        self.assertManyResults(number.fractional, test_list, result_list)

    def test_scientific(self):
        test_list = (1000, -1000, 5.5, 5781651000, "1000",
                     "99", float(0.3), 'foo', None)
        result_list = ('1.00 x 10³', '1.00 x 10⁻³', '5.50 x 10⁰', '5.78 x 10⁹',
                       '1.00 x 10³', '9.90 x 10¹', '3.00 x 10⁻¹', 'foo', None)
        self.assertManyResults(number.scientific, test_list, result_list)
        self.assertEqual(number.scientific(1000, precision=1), '1.0 x 10³')
        self.assertEqual(number.scientific(float(0.3), precision=1), '3.0 x 10⁻¹')
        self.assertEqual(number.scientific(1000, precision=0), '1 x 10³')
        self.assertEqual(number.scientific(float(0.3), precision=0), '3 x 10⁻¹')
