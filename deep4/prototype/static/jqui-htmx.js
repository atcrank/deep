/*  a javascript library that applies jQueryUI interactions to elements in a page as stipulated by (ideally)
    html attributes similar to htmx's family of hx- attributes.  related: unobtrusive jqueryui

Interactions:

 draggable
    $( "#draggable" ).draggable({ axis: "y" });
    $( "#draggable2" ).draggable({ axis: "x" });

    $( "#draggable3" ).draggable({ containment: "#containment-wrapper", scroll: false });
    $( "#draggable4" ).draggable({ containment: "parent" });
 droppable
    $( "#draggable" ).draggable();
    $( "#droppable" ).droppable({
      drop: function( event, ui ) {
        $( this )
          .addClass( "ui-state-highlight" )
          .find( "p" )
            .html( "Dropped!" );
      }
    });

 resizable
    $( "#resizable" ).resizable();
 selectable
    $( "#selectable" ).selectable();
 sortable
    $( "#sortable" ).sortable();

Widgets:
 accordion
 autocomplete(?)
 button
 checkboxradio
 controlgroup  +
    Example invocation, doesn't work well and drags in styles for buttons etc
    <div
      data-jqui="controlgroup"
      data-jqui-opts="{"direction":"vertical"}">
 datepicker
 dialog
 menu
 progressbar
 slider  +


// From BARD
// Initialize jQueryUI interactions on elements with data-jqui-* attributes
$(document).on('htmx:afterSwap', function(event) {
  $(event.detail.target).find('[data-jqui-*]').each(function() {  // this line doesn't work.  Bard says it does. shrugs
    const $this = $(this);
    const interaction = $this.data('jqui-');
    const options = $this.data('jqui-options');
    $this[interaction](options);
  });
});


*/

function add_jq(event) {
  console.log("afterSwap", event);
  let elmt = $(event.target);
  elmt.find('[data-jqui]').each(function () {
    console.log("this 1", $(this)[0], $(this)[0].getAttribute("data-jqui"), $(this)[0]["dataset"]);
    let id_ = `#${$(this)[0].getAttribute("id")}`;
    let interactions = $(this)[0].getAttribute("data-jqui");
    let interaction_options = JSON.parse($(this)[0].getAttribute("data-jqui-opts"));
    console.log("interact", interaction_options, JSON.parse($(this)[0].getAttribute("data-jqui-opts")));
  $(id_)[interactions](interaction_options);
  });
}

$(document).on('htmx:afterSwap', add_jq);
$(document).on('DOMContentLoaded', add_jq);
