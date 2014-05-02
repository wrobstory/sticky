# -*- coding: utf-8 -*-
"""
C3

"""
from IPython.html import widgets
from IPython.utils.traitlets import Unicode, Int, List, Dict
from jinja2 import Environment, PackageLoader

from sticky.core import Chart


ENV = Environment(loader=PackageLoader('sticky', 'templates/c3'))


class C3(widgets.DOMWidget, Chart):

    kind = 'c3'
    render_template = ENV.get_template('c3_widget.js')

    _view_name = Unicode('C3', sync=True)
    chart_id = Unicode(sync=True)
    chart_types = Dict(sync=True)
    model_data = List(sync=True)
    model_x = Unicode(sync=True)
    model_x_axis_type = Unicode(sync=True)
    model_height = Int(sync=True)
    model_width = Int(sync=True)

    def __init__(self, height=250, width=250, *args, **kwargs):
        """C3 Library Widget

        Parameters
        ----------
        height: int
        width: int
        **kwargs: d3plus params
        """
        super(C3, self).__init__(*args, **kwargs)

        # Visualization params
        self.height = height
        self.width = width
        self.raw_data = None
        self.model_data = []
        self.model_x_axis_type = 'categorized'
        self.chart_types = {}

    def data(self, data):
        """Dataset: Pandas DataFrame, long ("melted") format"""
        self.raw_data = data
        return self

    def x(self, x, timeseries=False):
        """
        Key for X Data (DataFrame column name, Series column name, dict key)

        Parameters
        ----------
        x: str
        """
        # import ipdb;ipdb.set_trace()
        if self.raw_data is None:
            raise ValueError('Data must be applied before specifying x')
        # grouped = self.raw_data.groupby(x)
        # for k, v in grouped.groups.items():
        #     v.insert(0, k)
        #     self.model_data.append(v)
        self.model_x = x
        if timeseries:
            self.model_x_axis_type = 'timeseries'
        return self

    def y(self, y):
        """
        Key for Y Data (DataFrame column name, Series column name, dict key

        Parameters
        ----------
        y: str
        """
        if self.raw_data is None:
            raise ValueError('Data must be applied before specifying y')
        self.model_data.append(self.raw_data[y])
        self.model_y = y
        return self

    def line(self, *args):
        """Line chart"""
        for arg in args:
            self.chart_types[arg] = 'line'
        return self

    def bar(self, *args):
        """Line chart"""
        for arg in args:
            self.chart_types[arg] = 'bar'
        return self

    def area(self, *args):
        """Line chart"""
        for arg in args:
            self.chart_types[arg] = 'area'
        return self

    def spline(self, *args):
        """Line chart"""
        for arg in args:
            self.chart_types[arg] = 'spline'
        return self

    def height(self, height):
        """Chart height: integer"""
        self.model_height = height
        return self

    def width(self, width):
        """Chart width: integer"""
        self.model_width = width
        return self
