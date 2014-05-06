# -*- coding: utf-8 -*-
"""
Test suite for core module.

To run these tests, please see test_core.ipynb
"""
import unittest
from uuid import uuid4


import sticky
import sticky.core as sc


class TestCore(unittest.TestCase):

    def setUp(self):
        self.chart = sc.Chart()
        self.chart.chart_id = '_'.join(['core', uuid4().hex])

    def test_get_dom_widget(self):
        dom_widget = self.chart._get_dom_widget()
        self.assertEqual(dom_widget._view_name, u'StickyDOMWidget')
        self.assertEqual(dom_widget.chart_id, self.chart.chart_id)

    def test_set_chart_attrs(self):
        polar_widget = sticky.Micropolar()
        polar_widget._set_chart_attrs(height=300, width=300)
        for k, v in zip(['model_height', 'model_width'], [300, 300]):
            self.assertEqual(getattr(polar_widget, k), v)

    def test_update(self):
        polar_widget = sticky.Micropolar()
        polar_widget.update(height=300)
        self.assertEqual(polar_widget.model_height, 300)
        self.assertTrue(False)
