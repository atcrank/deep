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
    e.g. data-jqui="selectable" data-jqui-opts="option filter li"

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

     data-jqui="draggable"
     data-jqui-opts="option cancel .richtextbox"
*/

function add_jq(event) {
  console.log("afterSwap", event);
  let elmt = $(event.target);
  console.log("find jqui", elmt.find('[data-jqui]'));
  console.log(elmt.find('[data-jqui]').each(function(e) {console.log("item", e)}));
  elmt.find('[data-jqui]').each(function (item) {
      let element =
    console.log("this 1", $(this))
    let id_ = `#${$(this)[0].getAttribute("id")}`;
    let interactions = $(this)[0].getAttribute("data-jqui");
    let interaction_options = $(this)[0].getAttribute("data-jqui-opts");
    console.log("adding", interactions, "with", interaction_options, "to", id_)

    if ((interactions) && (interaction_options)) {
      console.log("options", interaction_options.split(" "));
      $(id_)[interactions]()[interactions](...interaction_options.split(" "));
    }
    // if ((interactions) && (interaction_options)) {
    //   console.log("options", interaction_options.split(" "));
    //   $(id_)[interactions]()[interactions](...interaction_options.split(" "));
    // }
    if (interactions) {
        console.log("adding", interactions, "to", id_)
      $(id_)[interactions]();
    };
  }  );
}

// document.addEventListener('htmx:afterSwap', add_jq);
document.addEventListener('DOMContentLoaded', add_jq);

function add_position_updates(event) {
  console.log("size/position update", event.type);
  if (event.type === "mouseup"){
     //console.log("hit mouseup", event.target.parentNode.getAttribute("style"));
     //console.log("imagine we post:", event.target.parentNode.id, event.target.parentNode.getAttribute("style"), event.target);
    console.log("event", event)
     let left_of_self = event.target.previousElementSibling;
     let right_of_self = event.target.nextElementSibling;

     console.log("sortable - post:\n self", event.target,
         "\n left-", left_of_self,
         "\n right-", right_of_self);
  }
}
document.addEventListener('mouseup', add_position_updates, false)
