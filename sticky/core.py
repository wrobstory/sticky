# -*- coding: utf-8 -*-
"""
Sticky
-------

Python + IPython + D3

"""

from __future__ import print_function
from __future__ import division

from IPython.core.display import display, Javascript
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


class Chart(object):

    def init_widget_js(self):
        """Init Widget JS"""
        display(Javascript(self.render_template.render()))

    def plot(self):
        """Plot Sticky chart"""
        def render_chart(widget, **kwargs):
            display(self)
        dom_renderer = self._get_dom_creator()
        dom_renderer.on_displayed(render_chart)
        display(dom_renderer)
