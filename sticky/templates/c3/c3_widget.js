//C3 Library Renderer

require(["widgets/js/widget"], function(WidgetManager){

    function get_chart_spec(model){
              var chart_id = '.' + model.get('chart_id');
              spec = {
                  bindto: chart_id,
                  data: {
                    x: model.get('model_x'),
                    columns: model.get('model_data')
                  },
                  axis: {
                    x: {
                      type: model.get('model_x_axis_type')
                    }
                  }
                };
              return spec;
    }
    // Define the DOM Rendering View
    var C3Renderer = IPython.DOMWidgetView.extend({
        render: function(){
          // Get chart spec
          debugger
          var chart_spec = get_chart_spec(this.model);
          // Instantiate c3 chart
          this.$c3_chart = c3.generate(chart_spec);
        },
        update: function(){
          var chart_spec = get_chart_spec(this.model);
          this.$c3_chart.load(chart_spec);
        }
    });
    // Register the DOM Rendering View
    WidgetManager.register_widget_view('C3', C3Renderer);
});
