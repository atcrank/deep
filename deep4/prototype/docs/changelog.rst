recent changes
WARNING: RECENT CHANGES DISARM BASIC DJANGO SAFETY PROVISIONS IN THE RICHTEXT MODEL

- further refactoring to isolate Location logic from Content logic
- added a project / pages views construing a root Location as a Project, and first-level Children as defining 'pages'

- replaced SimpleRelation with Location with a generic Foreign Key pointing to different content types
     - PlainText, essentially the same is Simple_Thought
     - RichText, a new type using an old mozilla html editor for the form.  uses execCommand on the frontend (deprecated
       in favor of nothing) and a django TextField in the backend,
       * using the |safe filter CURRENTLY WITHOUT CHECKING IT IS SAFE CONTENT.
       * I've included a copy of the mozilla original because it is an incredible 100 lines of code.
       * Currently you can't use the jqui events and this editor because they contend - you can drag the richtext form
       but lose the ability to interact with the editable field using the mouse.

- added prototype/static/jqui-htmx.js  On load and afterSwap, find elements with a data-jqui attribute.
  This adds a jQueryUI interaction (draggable, resizable) functionality
  with data-jqui="draggable" (or sortable, selectable etc).  The styles aren't ideal for these functions.
  Looks for and tries but haven't progressed with data-jqui-opts="[options]"
  Haven't done the htmx parts which should post the relevant updates to the server.
  e.g:
        - draggable: post style info (holds changed x and y)
        - sortable: post movement data

- reorganised the urls into namespaces for location and content (again) to decouple them, more opportunity
- additional methods on each element (show help string from obj.__doc__ for example) (tick, completed)
- make ordered relationship elements (a tree subclass)  (MP_Node index is already ordered) (tick, learned something)
- use content types to make the content item generic (tick, except excluding self-referential loops)
- django-ninja api setup  # Broke spectacular API
- secure version for html in django textfield.
