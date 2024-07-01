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

 apply multiple options with ";" sep.
 e.g. data-jqui-opts="option cancel span;option axis y;"  will break if extra space after ";"
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
      console.log("optionset", interaction_options.split(";"));
      let ios = interaction_options.split(";")
      ios.forEach((iopt) => { console.log("iopt:", iopt, iopt.split(" ").length);
        if (iopt.split(" ").length === 3) {
          console.log("iopt.length == 3:", iopt, iopt.length);
      $(id_)[interactions]()[interactions](...iopt.split(" "));
      console.log("ios applied:", iopt.split(" ")[1], $(id_)["sortable"]("option", iopt.split(" ")[1]));
      }});
    }

    else if ((interactions) && not (interaction_options)) {
        console.log("adding", interactions, "to", id_)
      $(id_)[interactions]();
    };

  }  );
}

// document.addEventListener('htmx:afterSwap', add_jq);
document.addEventListener('DOMContentLoaded', add_jq);
document.addEventListener('afterSettle', add_jq);
function add_position_updates(event) {
    event.stopPropagation();
  console.log("size/position update", event.type, event.target.tagName);
  /*
  if ((event.type === "mouseup")&&(event.target.tagName == "LI")){
      let self = document.createElement("input");
         self.name = "self";
         self.value = event.target.getAttribute("id");
         self.hidden = "true";
         self.type="text"
     let left_of_self = document.createElement("input");
         left_of_self.name = "left";
         left_of_self.value =  event.target.previousElementSibling ? event.target.previousElementSibling.getAttribute("id") : null;
         left_of_self.hidden = "true";
         left_of_self.type="text"
     let right_of_self = document.createElement("input");
         right_of_self.name = "right";
         right_of_self.value = event.target.nextElementSibling ? event.targe.nextElementSiblin.getAttribute("id") : null;
         right_of_self.hidden = "true";
         right_of_self.type="text"
     let span = event.target.appendChild(document.createElement("span"));
     span.appendChild(self);
     span.appendChild(left_of_self);
     span.appendChild(right_of_self);
     htmx.process(event.target);
  }*/
}
document.addEventListener('mouseup', add_position_updates, false);
