# -*- coding: utf-8 -*-
"""
D3Plus:
http://d3plus.org/
https://github.com/alexandersimoes/d3plus
"""
from IPython.html import widgets
from IPython.utils.traitlets import Unicode, Int, List
from jinja2 import Environment, PackageLoader

from sticky.core import Chart


ENV = Environment(loader=PackageLoader('sticky', 'templates/d3plus'))


class d3Plus(widgets.DOMWidget, Chart):

    kind = 'd3plus'
    render_template = ENV.get_template('d3plus_widget.js')

    _view_name = Unicode('D3Plus', sync=True)
    chart_id = Unicode(sync=True)
    chart_type = Unicode(sync=True)
    model_data = List(sync=True)
    model_key = List(sync=True)
    model_x = Unicode(sync=True)
    model_y = Unicode(sync=True)
    model_height = Int(sync=True)
    model_width = Int(sync=True)

    def __init__(self, height=250, width=250, *args, **kwargs):
        """D3Plus Library Widget

        Parameters
        ----------
        height: int
        width: int
        **kwargs: d3plus params
        """
        super(d3Plus, self).__init__(*args, **kwargs)

        # Visualization params
        self.height = height
        self.width = width

    def line(self, **kwargs):
        """Line chart"""
        self.chart_type = 'line'
        self._set_chart_attrs(**kwargs)
        return self

    def stacked_area(self, **kwargs):
        """Stacked Area Chart"""
        self.chart_type = 'stacked'
        self._set_chart_attrs(**kwargs)
        return self

    def grouped_scatter(self, groupby=None, **kwargs):
        """Grouped scatter chart"""
        if not groupby:
            raise ValueError('Must provide groupby key!')
        self.chart_type = 'chart'
        self.groupby = groupby
        self._set_chart_attrs(**kwargs)
        return self

    def data(self, data):
        """List of Dicts (long format)"""
        self.model_data = data
        return self

    def height(self, height):
        """Chart height: integer"""
        self.model_height = height
        return self

    def width(self, width):
        """Chart width: integer"""
        self.model_width = width
        return self

    def x(self, x):
        """
        Key for X Data (DataFrame column name, Series column name, dict key)

        Parameters
        ----------
        x: str
        """
        self.model_x = x
        return self

    def y(self, y):
        """
        Key for Y Data (DataFrame column name, Series column name, dict key

        Parameters
        ----------
        y: str
        """
        self.model_y = y
        return self

    def key(self, key):
        """
        Key on which data is unique. When melting wide->long, this would be
        your "variable" column.

        Parameters
        -----------
        key: str
        """
        if hasattr(self, 'groupby'):
            self.model_key = [self.groupby, key]
        else:
            self.model_key = [key]
        return self

