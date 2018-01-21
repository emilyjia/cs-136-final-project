from block import Block
import random
import numpy
from ttc import ttc
from ttc import entropy

'''
we have x undergrads
what if they are evenly distributed among 6 types
and all transfer with same size
'''



def uniform_types(students, size):
  blocks = students/size
  # print blocks
  group = 6
  type_size = blocks/group
  # print type_size
  houses = [[] for x in range(0, 12)]
  for block_type in range(1, 7):
    for i in range(0, type_size):
      # randomly generate house
      house = random.randint(1, 12)
      houses[house-1].append(Block(block_type, house, "perm", block_type))
  # print houses
  return houses

def uniform_interhouse(students, size):
  houses = uniform_types(students, size)
  [allocation, count] = ttc(houses, size)
  # print entropy(allocation)
  return 1.0*count/(1.0*students)*1.0*size
  #return [entropy_lst, count]


7.943282347
15.84893192
31.6227766
63.09573445
125.8925412
251.1886432
501.1872336
1000

for groups in [1, 8, 16, 32, 64, 126, 252, 501, 1000]:
  sum_1 = 0
  for x in range(0, 1000):
    #if x%100 == 0:
      #print x
    sum_1+= uniform_interhouse(2*groups, 2)
  print (1.0*sum_1)/1000.0






