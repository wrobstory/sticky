# -*- coding: utf-8 -*-
"""
Micropolar:
http://micropolar.org/
https://github.com/biovisualize/micropolar/
"""
from uuid import uuid4

from IPython.html import widgets
from IPython.utils.traitlets import Unicode
from jinja2 import Environment, PackageLoader

from sticky.core import Chart


ENV = Environment(loader=PackageLoader('sticky', 'templates/micropolar'))


class MicropolarDOM(widgets.DOMWidget):
    """DOM Creator Widget"""
    _view_name = Unicode('MicropolarDOM', sync=True)
    chart_id = Unicode(sync=True)


class Micropolar(widgets.DOMWidget, Chart):
    _view_name = Unicode('Micropolar', sync=True)
    chart_id = Unicode(sync=True)

    id_ = uuid4()
    render_template = ENV.get_template('micropolar_widget.js')

    def __init__(self, *args, **kwargs):
        """Micropolar D3 Library Widget"""
        super(Micropolar, self).__init__(*args, **kwargs)
        self.init_widget_js()

    def _get_dom_creator(self):
        """Instance of MicropolarDOM"""
        self.chart_id = '_'.join(['micropolar', uuid4().hex])
        dom_widget = MicropolarDOM()
        dom_widget.chart_id = self.chart_id
        return dom_widget
