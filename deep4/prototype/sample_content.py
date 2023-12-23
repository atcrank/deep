from .models import SimpleThought, SimpleRelation

s = SimpleThought.objects.create(content="Root thought.")

root_thought = SimpleRelation.add_root(content=s)

s1 = SimpleThought.objects.create(content="child 1.")
s2 = SimpleThought.objects.create(content="child 2.")
s3 = SimpleThought.objects.create(content="child 3.")
s4 = SimpleThought.objects.create(content="child 4.")

root_thought.add_child(content=s1)
root_thought.add_child(content=s2)
root_thought.add_child(content=s3)
root_thought.add_child(content=s4)
