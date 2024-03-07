Immediate goals
---------------


 - refactor ContentModelFormView into LocationModelFormView and ContentModelFormView - the big split in 'setup()' is leading. (done)

 - improvements to jqui:

   - prevent application of these effects on RichTextForm because it prevents drag-select of text. (added jqui-opts="option cancel span" but only handles setting one option)
   - how to organise:

      - sortable vs draggable vs selectable need different options set
      - currently options depend on the template e.g. option cancel span
      - where to hold data setting children to sortable or selectable or draggable
      - currently hardcoded - all siblings are 'sortable' but sort outcomes are not saved.

 - Templates. Goal would be to have tree.html as a fundamental template but whether its ul-li or div-div or details-summary or table-tr-td(?)

 - REUSE strategy for project, page, page-sequence reuse for repeated tasks
 - INTERFACES for interpretation using user input as evidence base

 - caching - adding user will slow things down
 - reference counting on content_objects (garbage collection)?
