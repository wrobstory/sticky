# -*- coding: utf-8 -*-
"""
D3Plus:
http://d3plus.org/
https://github.com/alexandersimoes/d3plus
"""
from IPython.html import widgets
from IPython.utils.traitlets import Unicode, Int
from jinja2 import Environment, PackageLoader

from sticky.core import Chart


ENV = Environment(loader=PackageLoader('sticky', 'templates/d3plus'))


class d3Plus(widgets.DOMWidget, Chart):

    kind = 'd3plus'
    render_template = ENV.get_template('d3plus_widget.js')

    _view_name = Unicode('D3Plus', sync=True)
    chart_id = Unicode(sync=True)
    height = Int(sync=True)
    width = Int(sync=True)

    def __init__(self, height=250, width=250, *args, **kwargs):
        """Micropolar D3 Library Widget"""
        super(d3Plus, self).__init__(*args, **kwargs)
        self.height = height
        self.width = width
        self.init_widget_js()
