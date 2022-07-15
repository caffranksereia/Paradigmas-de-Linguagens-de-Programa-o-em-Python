from opcode import hasconst
import sys
import time

# def gera():
#     # for n in range(100):
#     #     yield n 
#     #     time.sleep(0.1)
#     n = 1
#     yield n
#     n = 2
#     yield n
#     n = 3
#     yield n
  

# g = gera()

# print(hasattr(g,'__iter__'))
# print(hasattr(g,'__next__'))
# print(next(g))
# print(next(g))
# print(next(g))
# for v in g:
#     print(v)

l = [x for x in range(1000)]
l0 = (x for x in range(1000))


print(sys.getsizeof(l))
print(sys.getsizeof(l0))