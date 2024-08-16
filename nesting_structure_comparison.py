'''
Complete the function/method (depending on the language) to return true/True when its argument 
is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.
'''
from collections.abc import Iterable

def same_structure_as(original, other):
    scheme = []
    get_el_scheme(original, scheme)
    
    other_scheme = []
    get_el_scheme(other, other_scheme)

    return scheme == other_scheme

def get_el_scheme(original, scheme):
    if isinstance(original, Iterable) \
        and type(original) != type('') \
        and type(original) == type(scheme):
        scheme.append('iterator')
        for index, element in enumerate(original):
            get_el_scheme(element, scheme)
    else:
        scheme.append('instance') 
          
# Best solution from codewars.com
def same_structure_as(original, other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2): return False
        else: return True
    else: return not isinstance(original, list) and not isinstance(other, list)


print(same_structure_as([1,[1,1]],[2,[2,2]]), True, "[1,[1,1]] same as [2,[2,2]]")
print(same_structure_as([1,[1,1]],[[2,2],2]), False, "[1,[1,1]] not same as [[2,2],2]")