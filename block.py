# blocking group class
import math
import random
from scipy.stats import norm

'''
Block class
create an item by declaring block = Block(block_type, house, pref_type)
or block = Block(block_type, house, pref_type, block_id)

block_type is 1, 2, 3, 4, 5, 6
house is initial house
pref_type should be "basic" or "perm"
basic gives three options fo students, perm gives six
block_id is for TTC

call the preference list with block.pref
also useful may be accessing block.house
'''
class Block:

  # you need to specify original house, and type
  def __init__(self, block_type, house, pref_type, block_id=0):
    self.house = house
    self.block_id = block_id
     # defines neighborhoods
    self.nbhdA = [1, 2, 3, 4]
    self.nbhdB = [5, 6, 7, 8]
    self.nbhdC = [9, 10, 11, 12]
    self.block_type = block_type

    if pref_type == "basic":
      pref = self.pref_basic(block_type)
    elif pref_type == "perm":
      pref = self.pref_perm(block_type)

    self.pref = self.ir_clean(self.pref_shuffle(pref, 7))

  def __repr__(self):
    return str(self.block_id)

  # assigns three types of preferences by neighborhood
  def pref_basic(self, block_type):
    if block_type%3 == 1:
      pref = self.nbhdA + self.nbhdB + self.nbhdC
    elif block_type%3 == 2:
      pref = self.nbhdB + self.nbhdC + self.nbhdA
    else:
      pref = self.nbhdC + self.nbhdA + self.nbhdB
    return pref

  # type 1: ABC
  # type 2: ACB
  # type 3: BAC
  # type 4: BCA
  # type 5: CAB
  # type 6: CBA

  def pref_perm(self, block_type):
    if block_type == 1:
      pref = self.nbhdA + self.nbhdB + self.nbhdC
    elif block_type == 2:
      pref = self.nbhdA + self.nbhdC + self.nbhdB
    elif block_type == 3:
      pref = self.nbhdB + self.nbhdA + self.nbhdC
    elif block_type == 4:
      pref = self.nbhdB + self.nbhdC + self.nbhdA
    elif block_type == 5:
      pref = self.nbhdC + self.nbhdA + self.nbhdB
    else:
      pref = self.nbhdC + self.nbhdB + self.nbhdA
    return pref


  '''
  # too much noise

  def norm_weight(self, pref_index, min, max):
    x = (max-min)/13.0*pref_index + min
    return norm.cdf(x, 0, 5)
  '''


  # adds logistical noise
  # calculates the correct weight
  def log_weight(self, pref_index, min, max):
    steep = -1
    x = (max - min)/13.0 * pref_index + min
    return 1.0/(1 + math.exp(-steep*x))


  '''
  takes the new list of prefed, the houses that still need to be prefed,
  and the weights for remaining houses

  outputs a new list of preferences that is 1 house longer than before
  '''
  def shuffle(self,new_pref, old_pref, weights):
    x = random.random()*sum(weights)
    # print "====shuffle===="
    # print x
    # print weights
    count = 0
    index = 0
    for i in range(0, len(weights)):
      if count <= x <= count + weights[i]:
        index = i
      count += weights[i]
    # print index
    new_pref.append(old_pref[index])
    old_pref.pop(index)
    weights.pop(index)
    return [new_pref, old_pref, weights]

  '''
  shuffles preference order
  houses are 1-12
  '''
  def pref_shuffle(self, pref, amt):
    # print "======pref_shuffle======"
    weights = []
    for i in range(1, 13):
      weights.append(self.log_weight(i, amt, -amt))
    # for weight in weights:
      #print weight
    # print "====generated weights====="
    new_pref = []
    old_pref = pref
    for i in range(1, 13):
      x = self.shuffle(new_pref, old_pref, weights)
      new_pref = x[0]
      old_pref = x[1]
      weights = x[2]
      # print "====new_pref====="
      # print new_pref
    new_pref.reverse()
    return new_pref

  # takes preferences and makes them ir
  def ir_clean(self, pref):
    for x in range(pref.index(self.house), len(pref)):
      pref[x] = self.house
    return pref

  def log_penalty(self, pref, size):
    return self.pref_shuffle(pref, 0.1-size*0.01)

def get_weight():
  block = Block(1, 12, "perm")
  print "======"
  for x in [0.09, 0.05, 0.02]:
    print x
    pref = [y for y in range(1, 13)]
    block.pref_shuffle(pref, x)
    print "======"


def get_pref():
  block = Block(1, 12, "perm")
  for x in range(6, 9):
    print x
    for y in range(0, 3):
      pref = [y for y in range(1, 13)]
      print(block.pref_shuffle(pref, x))
'''
this is a poorly coded test
'''

def count_position():
  position = [0 for x in range(0, 12)]
  stdev = [0 for x in range(0, 12)]
  averages_009 = [6.4681, 6.49097, 6.48681, 6.49531, 6.49819, 6.49646, 6.48986, 6.51263, 6.51654, 6.50881, 6.5225, 6.51382]
  #averages_7 = [1.44037, 2.23091, 3.22509, 4.40792, 5.82546, 7.23348, 8.28148, 8.82598, 9.05798, 9.13528, 9.15945, 9.1766]
  #averages_8 = [1.35202, 2.15382,3.12728,4.29246,5.72113,7.25772,8.40666,8.9508,9.13011,9.19196,9.20967,9.20637]
  #averages_6 = [1.58447, 2.37221, 3.371, 4.56618, 5.89382, 7.1963, 8.13339, 8.68667, 8.93747, 9.0544, 9.09207, 9.11202]
  block = Block(1, 12, "perm")
  for x in range(0, 100000):
    pref = [x for x in range(1, 13)]
    shuffled = block.pref_shuffle(pref, 0.02)
    for i in range(0, 12):
      house = shuffled[i]
      position[house-1] += i+1
      stdev[house-1] += (i+1 - averages_009[house-1])*(i+1 - averages_009[house-1])
  for x in position:
    print x/100000.0
  for x in stdev:
    print math.sqrt(x/100000.0)
  print [x/100000.0 for x in position]

#get_weight()
count_position()
# get_pref()


