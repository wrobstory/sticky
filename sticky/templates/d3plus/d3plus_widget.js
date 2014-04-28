//D3 Plus Library Renderer

require(["widgets/js/widget"], function(WidgetManager){

    function build_chart(chart, model){
              var chart_id = '.' + model.get('chart_id');
              chart
              .container(chart_id)
              .height(model.get('model_height'))
              .width(model.get('model_width'))
              .data(model.get('model_data'))
              .type(model.get('chart_type'))
              .id(model.get('model_key'))
              .text(model.get('model_key'))
              .y(model.get('model_y'))
              .x(model.get('model_x'));
    }

    // Define the DOM Rendering View
    var D3PlusRenderer = IPython.DOMWidgetView.extend({
        render: function(){
            // Instantiate d3plus
            this.$d3plus_chart = d3plus.viz();
            // Build chart from model params
            build_chart(this.$d3plus_chart, this.model);
            // Draw
            this.$d3plus_chart.draw();
        },

        update: function(){
            build_chart(this.$d3plus_chart, this.model);
            this.$d3plus_chart.draw();
        }
    });
    // Register the DOM Rendering View
    WidgetManager.register_widget_view('D3Plus', D3PlusRenderer);
});
