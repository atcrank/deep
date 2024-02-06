recent changes

- added prototype/static/jqui-htmx.js  On load and afterSwap, find elements with a data-jqui attribute.
  This adds a jQueryUI interaction (draggable, resizable) functionality
  with data-jqui="draggable" (or sortable, selectable etc).  The styles aren't ideal for these functions.
  Looks for and tries but haven't progressed with data-jqui-opts="[options]"
  Haven't done the htmx parts which should post the relevant updates to the server.
  e.g:
        - draggable: post style info (holds changed x and y)
        - sortable: post movement data

- reorganised the urls into namespaces for location and content.
