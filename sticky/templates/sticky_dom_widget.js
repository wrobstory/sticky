require(["widgets/js/widget", "widgets/js/manager"], function(widget, manager){

    // Define the DOM Creation view for Sticky charts
    var StickyDOMWidget = widget.DOMWidgetView.extend({
        render: function(){
            var chart_id = this.model.get('chart_id');
            var chart_elm = '<div id="' + chart_id + '"></div>';
            $(chart_elm).appendTo(this.$el);
        },
    });
    // Register the DOM Renderer with the Widget Manager
    manager.WidgetManager.register_widget_view('StickyDOMWidget', StickyDOMWidget);
});
