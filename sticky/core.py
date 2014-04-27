# -*- coding: utf-8 -*-
"""
Sticky
-------

Python + IPython + D3

"""
from __future__ import print_function
from __future__ import division

from uuid import uuid4

from IPython.core.display import display, Javascript
from IPython.html import widgets
from IPython.utils.traitlets import Unicode
from jinja2 import Environment, PackageLoader


ENV = Environment(loader=PackageLoader('sticky', 'templates'))


def initialize_notebook():
    """Initialize the IPython notebook display elements"""
    try:
        from IPython.core.display import HTML
    except ImportError:
        print("IPython Notebook could not be loaded.")

    lib_js = ENV.get_template('ipynb_init_js.html')

    display(HTML(lib_js.render()))


class StickyDOMWidget(widgets.DOMWidget):
    """DOM Creator Widget"""
    _view_name = Unicode('StickyDOMWidget', sync=True)
    chart_id = Unicode(sync=True)


class Chart(object):

    def _get_dom_creator(self):
        """Instance of MicropolarDOM"""
        self.chart_id = '_'.join([self.kind, uuid4().hex])
        dom_widget = StickyDOMWidget()
        dom_widget.chart_id = self.chart_id
        return dom_widget

    def init_widget_js(self):
        """Init Widget JS"""
        dom_template = ENV.get_template('sticky_dom_widget.js')
        display(Javascript(dom_template.render()))
        display(Javascript(self.render_template.render()))

    def update(self, **kwargs):
        """Update View Model with given keywords"""
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.send_state()

    def plot(self):
        """Plot Sticky chart"""
        def render_chart(widget, **kwargs):
            display(self)
        dom_renderer = self._get_dom_creator()
        dom_renderer.on_displayed(render_chart)
        display(dom_renderer)
