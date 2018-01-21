from block import Block
import random
import numpy
import math
'''
each node represents a house
'''
# houses is a list of lists of blocks
# penalize group
def penalize_size(houses, size):
  for house in houses:
    for block in house:
      block.pref = block.ir_clean(block.log_penalty(block.pref, size))

def get_top(houses):
  top_pref = []
  for i in range(0, 12):
    house = houses[i]
    if house == []:
      top = None
    else:
      pref = house[0].pref
      top = pref[0]
      i = 0
      while houses[top-1] == []:
        i +=1
        top = pref[i]
    # print top
    top_pref.append(top)
  return top_pref

# top_blocks contains the top 13 in each house, and their top available choice
# check for cycles
# houses are 1-12 but in positions 0-11
def find_cycle(top_pref):
  cycle = []
  not_none = -1
  i = 0
  while not_none == -1:
    if top_pref[i] != None:
      not_none = i
    i+=1
  cycle.append(not_none)
  next_house = top_pref[not_none]
  while next_house not in cycle:
    cycle.append(next_house)
    next_house = top_pref[next_house-1]
  cycle_start = cycle.index(next_house)
  cycle = cycle[cycle_start:]
  return cycle

def remove_cycle(cycle, houses, allocation):
  transfer_count = 0
  for i in range (0, len(cycle)):
    # store the house in the cycle
    house = cycle[i]
    # find the block
    x = houses[house-1][0]
    # change house of block
    next_house = cycle[(i+1)%len(cycle)]
    if x.house != next_house:
      transfer_count += 1
      x.house = next_house
    # add to allocation
    allocation[next_house-1].append(x)
    # delete house from houses
    del houses[house-1][0]
  return [houses, allocation, transfer_count]

def ttc(houses, size):
  penalize_size(houses, size)
  for house in houses:
    house = random.shuffle(house)
  # for house in houses:
    # for block in house:
      # print block
      # print block.pref
  transfer_count = 0
  allocation = [[] for x in range(0, 12)]
  while houses != [[] for x in range(0, 12)]:
    top_pref = get_top(houses)
    # print "top_pref"
    # print top_pref
    cycle = find_cycle(top_pref)
    # print "cycle"
    # print cycle
    [houses, allocation, count] = remove_cycle(cycle, houses, allocation)
    transfer_count += count
    # print "houses"
    # print houses
    # print "allocation"
    # print allocation
  return [allocation, transfer_count]

def test_penalize():
  perm_one = Block(1, 12, "perm")
  perm_two = Block(2, 8, "perm")
  perm_three = Block(3, 12, "perm")
  perm_four = Block(4, 4, "perm")
  perm_five = Block(5, 8, "perm")
  perm_six = Block(6, 4, "perm")
  house = [perm_one, perm_two, perm_three, perm_four, perm_five, perm_six]
  #for block in house:
    #print block.pref
  #print "======"
  penalize_size([house], 8)
  #for block in house:
    #print block.pref

def test_remove():
  cycle = [1, 2, 3, 4]
  houses = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]
  allocation = [[],[],[],[]]
  x = remove_cycle(cycle, houses, allocation)
  #print x[0]
  #print x[1]

def test_top():
  perm_one = Block(1, 12, "perm", "perm_one")
  perm_two = Block(2, 8, "perm", "perm_two")
  perm_three = Block(3, 12, "perm", "perm_three")
  perm_four = Block(4, 4, "perm", "perm_four")
  perm_five = Block(5, 8, "perm", "perm_five")
  perm_six = Block(6, 4, "perm", "perm_six")
  house = [perm_one, perm_two, perm_three, perm_four, perm_five, perm_six]
  houses = [[], [], [], [perm_four, perm_six], [],[],[],[perm_two, perm_five], [], [], [], [perm_one, perm_three]]
  # print "======"
  # print get_top(houses)
  # print houses
  x =  ttc(houses, 8)
  # print x


# count number of type in each house
def count_type(block_type, allocation):
  distribution = []
  for house in allocation:
    count = 0
    for block in house:
      if block.block_type == block_type:
        count += 1
    distribution.append(count)
  # print "distribution for " + str(block_type)
  return distribution

  '''
  # compute sum p_i log p_i
  total = sum(distribution)
  h = 0

  for count in distribution:
    p_i = (count*1.0)/(total*1.0)
    h += p_i * math.log10(p_i)
  return -h
  '''

# compute entropy of all types over all houses
def entropy(allocation):
  distribution = [count_type(x, allocation) for x in range(1, 7)]
  total = sum([sum(house) for house in distribution])
  h = 0
  for house in distribution:
    for count in house:
      p_i = (1.0*count)/(1.0*total)
      h -= p_i * math.log(p_i, 2.0)
  return h








