// Make every node draggable and droppable


// Add event listeners for the update events
console.log("loading drag-drop handler", document.getElementsByClassName("node"));


for (let d in document.getElementsByClassName("node")) {d.addEventListener("htmx:afterOnLoad", function() {
    console.log("node ", d);
    // Get the node that triggered the event
    d.draggable({
        revert: "invalid", // revert to original position if not dropped on a valid target
        helper: "clone", // create a clone of the node while dragging
        cursor: "move", // change the cursor to indicate movement
        snap: "true"
    })
        d.droppable({
        accept: ".node", // accept only nodes as droppable items
        greedy: true, // prevent parent nodes from activating when dropping on a child node
        drop: function(event, ui) {
            // Get the dropped node and the target node
            var dropped = ui.draggable;
            var target = $(this);

            // Check if the dropped node is already a child of the target node
            if (target.find(dropped).length > 0) {
                // If yes, do nothing
                return;
            }

            // Check if the target node has a <ul> tag as a child
            var ul = target.children("ul");
            if (ul.length == 0) {
                // If not, create one and append it to the target node
                ul = $("<ul></ul>");
                target.append(ul);
            }

            // Append the dropped node to the <ul> tag of the target node
            ul.append(dropped);

            // Trigger an update event on the dropped node
            dropped.trigger("update");
        }
      })
     //end handleDropDrag
})
};
