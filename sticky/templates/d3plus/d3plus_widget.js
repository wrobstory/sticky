//D3 Plus Library Renderer

require(["widgets/js/widget"], function(WidgetManager){

    // Define the DOM Rendering View
    var D3PlusRenderer = IPython.DOMWidgetView.extend({
        render: function(){
            debugger
            var chart_id = '.' + this.model.get('chart_id');
            var sample_data = [
              {"year": 1991, "name":"alpha", "value": 15},
              {"year": 1992, "name":"alpha", "value": 20},
              {"year": 1994, "name":"alpha", "value": 30},
              {"year": 1995, "name":"alpha", "value": 60},
              {"year": 1993, "name":"beta", "value": 40},
              {"year": 1994, "name":"beta", "value": 60},
              {"year": 1995, "name":"beta", "value": 10},
              {"year": 1994, "name":"gamma", "value": 35},
              {"year": 1995, "name":"gamma", "value": 40}
            ];

            // instantiate d3plus
            this.$d3plus_chart = d3plus.viz()
              .container(chart_id)
              .height(this.model.get('height'))
              .width(this.model.get('width'))  // container DIV to hold the visualization
              .data(sample_data)  // data to use with the visualization
              .type("line")       // visualization type
              .id("name")         // key for which our data is unique on
              .text("name")       // key to use for display text
              .y("value")         // key to use for y-axis
              .x("year")          // key to use for x-axis
              .draw();             // finally, draw the visualization!
        },

        update: function(){
            this.$d3plus_chart
                .width(this.model.get('width'))
                .height(this.model.get('height'));
            this.$d3plus_chart.draw();
        }
    });
    // Register the DOM Rendering View
    WidgetManager.register_widget_view('D3Plus', D3PlusRenderer);
});
