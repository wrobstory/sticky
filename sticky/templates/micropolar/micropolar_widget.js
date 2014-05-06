//Micropolar Library Renderer

require(["widgets/js/widget"], function(WidgetManager){

    // Define the DOM Rendering View
    var MicropolarRender = IPython.DOMWidgetView.extend({
        render: function(){
            var chart_id = '.' + this.model.get('chart_id');
            var polarPlot = micropolar.DotPlot();
            this.$plot_config = {
                geometry: polarPlot,
                data: [[0, 500], [1, 1000], [3, 2000]],
                height: this.model.get('model_height'),
                width: this.model.get('model_width'),
                angularDomain: [0, 2000],
                angularTicksStep: 400,
                minorTicks: 1,
                flip: false,
                originTheta: 0,
                radialAxisTheta: -15,
                containerSelector: chart_id
            };
            this.$micropolar_chart = micropolar.Axis().config(this.$plot_config);
            this.$micropolar_chart();
        },

        update: function(){
            this.$plot_config.height = this.model.get('height');
            this.$plot_config.width = this.model.get('width');
            this.$micropolar_chart.config(this.$plot_config);
            this.$micropolar_chart();
            return MicropolarRender.__super__.update.apply(this);
        }
    });
    // Register the DOM Rendering View
    WidgetManager.register_widget_view('Micropolar', MicropolarRender);
});
