Immediate goals
---------------

 - create Frame model to hold meta data info for content and children
    Frames: template constructors attached at location, calls for entity attributes on content with key to location with JSONField({location_id: , for_frame: frame_type, html: {} , style: {}, htmx?: {}}
    - sorted single list
    - sorted single list allowing equality
    - xy layout space
    - xy gridded layout space

 - improvements to jqui: [switch to treebeard admin js]

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

Concepts
--------

Atomic representation of Concept and multi-entry extension.

Organising actions:
- classifying under a higher order or more abstract concept
- decomposing details into multiple subconcepts
- adding examples
- title field
  - display markup
  - analysis markup tags

- details field
  - linebreaks and indentation
  - ie (alternate title) and eg (more concrete example) and
  - => implies
  - <=>  iff
  - ~ related to / !~ independent
  - !=> negates / <=! is negated when
  - author markup (richer text)
  - analytic markup tags
  - gpt markup tags

- relationships
  - simple indentation
  - linkage arrows (limits to showing 2-arity)
  - grouping borders
  - classification (styles for single mutually exclusive systems)
  - tags, badges (multiple schemes)
  - contradiction??
  - autolayout


move from location[content]
html - location[content, [frame[child locations]];
data - location[frame, content];
