//C3 Library Renderer

require(["widgets/js/widget", "widgets/js/manager", "c3"], function(widget, manager, c3){

    function get_chart_spec(model){
      debugger
      var chart_id = '#' + model.get('chart_id');
      var spec = {
          bindto: chart_id,
          size: {
            width: 800,
            height: 500
          },
          data: {
              columns: [
                  ['data1', 30, 200, 100, 400, 150, 250],
                  ['data2', 50, 20, 10, 40, 15, 25]
              ]
          }
      };
      return spec;
    }
    // Define the DOM Rendering View
    var C3Renderer = widget.DOMWidgetView.extend({
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
    manager.WidgetManager.register_widget_view('C3', C3Renderer);
});
