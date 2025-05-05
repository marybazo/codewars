#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(lnumbers: list):
    return sorted(lnumbers, key=lambda x: x==0 and type(x) is not bool)


print(move_zeros([1, 0, 1, 2, 0, 1, 3])) # returns [1, 1, 2, 1, 3, 0, 0]
