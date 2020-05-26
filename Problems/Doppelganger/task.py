# the object_list has already been defined
# write your code here
from collections.abc import Hashable

h_list = [hash(o) for o in object_list if isinstance(o, Hashable)]
dup_dict = {i: h_list.count(i) for i in h_list if h_list.count(i) > 1}
print(sum(dup_dict.values()))
