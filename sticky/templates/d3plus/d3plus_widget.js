//D3 Plus Library Renderer

require(["widgets/js/widget"], function(WidgetManager){

    var d3plus_charts = {};

    function build_chart(chart, model, chart_id){
              var data = JSON.parse(model.get('model_data'));
              chart.container(chart_id)
                   .height(model.get('model_height'))
                   .width(model.get('model_width'))
                   .data(data)
                   .type(model.get('chart_type'))
                   .id(model.get('model_key'))
                   .text(model.get('model_key'))
                   .y(model.get('model_y'))
                   .x(model.get('model_x'));
    }

    var bounced_builder = _.debounce(build_chart, 300, true);

    // Define the DOM Rendering View
    var D3PlusRenderer = IPython.DOMWidgetView.extend({
        render: function(){
            var chart_id = '.' + this.model.get('chart_id');
            // Instantiate d3plus
            d3plus_charts[chart_id] = d3plus.viz();
            build_chart(d3plus_charts[chart_id], this.model, chart_id);
            // Draw
            d3plus_charts[chart_id].draw();
        },

        update: function(){
            var chart_id = '.' + this.model.get('chart_id');
            var chart = d3plus_charts[chart_id];
            // Something of a hack
            bounced_builder(chart, this.model, chart_id);
            chart.draw();
        }
    });
    // Register the DOM Rendering View
    WidgetManager.register_widget_view('D3Plus', D3PlusRenderer);
});
