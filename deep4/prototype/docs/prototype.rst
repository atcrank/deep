Immediate goals
---------------

 - secure version for html in django textfield.
 - refactor ContentModelFormView into LocationModelFormView and ContentModelFormView - the big split in 'setup()' is leading.

 - improvements to jqui:
   - prevent application to RichTextForm
   - correct sortable classes so that they don't apply 'changing' color to the parent
   - work out how to communicate and store location and size (easy)
   - work out how to communicate sortable actions to tree move api

 - parameterise(?) parent and child html tags. (Not possible in Django Template Language, because undesirable for security.  The concept is that the tree structure is applicable as ul-li, but also trivially, ol-li, and less trivially, col-row-col tiling so the first and last trees are sidebars.
 - user-awareness and per object group-permissions
   possible patterns:
     - Location with a User awareness and the option to root a new location tree as the content_object. This should cope with multiple users with multiple inputs.
     - ownership of content, simultaneous editing, diffing?
       - start with labeled border class
     - reuse target-groups pattern, override Mp_Node.add_child() to copy the target_groups down.

 - page and sub-page tree
   - some Location roots are marked as Project roots, by default 1st-level children are individual pages.
   -
 - REUSE strategy for project, page, page-sequence reuse for repeated tasks
 - INTERFACES for interpretation using user input as evidence base

 - caching - adding user will slow things down
 - reference counting on content_objects (garbage collection)?
