# This file was *autogenerated* from the file 70.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_10 = Integer(10); _sage_const_7 = Integer(7)
ans = _sage_const_10 **_sage_const_10 

def chk(x, y) :
    return sorted(str(x)) == sorted(str(y))

for i in (ellipsis_range(_sage_const_2  ,Ellipsis, (_sage_const_10 **_sage_const_7  - _sage_const_1 ))) :
    t = euler_phi(i)
    if chk(i, t) :
        if i / t < ans :
            ans = i / t
            print i, t, ans
print ans