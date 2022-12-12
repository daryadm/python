    """
    a is the number of recursive calls
    b is tne size of each recursive call
    d is the running time of the last combining step of previous recursive results. Constant time 0; Linear time 1. 


    a**logb(n) - the number of leaves of the recursion tree
    a**logb(n) == n**logb(a)

    the master method
    
    If T(n) <= aT(n/b) + O(n**d)
    then
    T(n) = 
    O(n**d*logn) if a = b**d
    O(n**d) if a < b**d
    O(n**logb(a)) if a > b**d
    """

