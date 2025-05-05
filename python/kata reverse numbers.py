def invert(lst):
    n_lst = list()
    for i in lst: 
        n_lst.append(-i) if i > 0 else n_lst.append(abs(i))
    return n_lst  

def pro_invert(lst):
    return [-x for x in lst]      

lst = pro_invert([1,2,6,4,5])
print(lst)

b=True
print(str(b))
bool()