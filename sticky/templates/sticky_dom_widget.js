require(["widgets/js/widget"], function(WidgetManager){

    // Define the DOM Creation view for Sticky charts
    var StickyDOMWidget = IPython.DOMWidgetView.extend({
        render: function(){
            var chart_id = this.model.get('chart_id');
            var chart_elm = '<div class="' + chart_id + '"></div>';
            $(chart_elm).appendTo(this.$el);
        },
    });
    // Register the DOM Renderer with the Widget Manager
    WidgetManager.register_widget_view('StickyDOMWidget', StickyDOMWidget);
});
