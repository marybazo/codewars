def is_square(n):
   return n >= 0 and (n**0.5)%1 == 0

print(is_square(-1))
print(is_square(9))