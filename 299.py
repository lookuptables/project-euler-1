# This file was *autogenerated* from the file 299.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_100 = Integer(100); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0)
ans = _sage_const_0 
for a in (ellipsis_range(_sage_const_1  ,Ellipsis, _sage_const_100 )) :
    for b in (ellipsis_range((_sage_const_2  * a + _sage_const_1 ) ,Ellipsis, _sage_const_100 )) :
        for d in (ellipsis_range((_sage_const_2  * a + _sage_const_1 ) ,Ellipsis, _sage_const_100 )) :
            if b + d >= _sage_const_100  :
                break
            if _sage_const_2  * a * a == (b - _sage_const_2  * a) * (d - _sage_const_2  * a) :
                print a, b, d
                ans += _sage_const_1 
print ans