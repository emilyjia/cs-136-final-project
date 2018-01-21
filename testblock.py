from block import Block

'''
unit tests for the block class
'''

def test_block():
  print "============"
  # testing pref_basic
  basic_one = Block(1, 12, "basic")
  basic_two = Block(2, 4, "basic")
  basic_three = Block(3, 8, "basic")

  assert basic_one.pref == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  assert basic_two.pref == [5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4]
  assert basic_three.pref == [9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8]
  print "pref_basic tests passed"

  # testing ir_clean
  ir_one = Block(1, 1, "basic")
  ir_two = Block(2, 11, "basic")
  ir_three = Block(3, 8, "basic")

  assert ir_one.pref == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  assert ir_two.pref == [5, 6, 7, 8, 9, 10, 11, 11, 11, 11, 11, 11]
  assert ir_three.pref == [9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8]
  print "ir_clean tests passed"

  # testing pref_perm
  perm_one = Block(1, 12, "perm")
  perm_two = Block(2, 8, "perm")
  perm_three = Block(3, 12, "perm")
  perm_four = Block(4, 4, "perm")
  perm_five = Block(5, 8, "perm")
  perm_six = Block(6, 4, "perm")

  assert perm_one.pref == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  assert perm_two.pref == [1, 2, 3, 4, 9, 10, 11, 12, 5, 6, 7, 8]
  assert perm_three.pref == [5, 6, 7, 8, 1, 2, 3, 4, 9, 10, 11, 12]
  assert perm_four.pref == [5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4]
  assert perm_five.pref == [9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8]
  assert perm_six,pref == [9, 10, 11, 12, 5, 6, 7, 8, 1, 2, 3, 4]
  print "pref_perm tests passed"

  '''
  # testing log distribution
  # 20, -20 gives 75% chance of first house being in top 5
  # k = -0.25 scales well at both extremes
  sum = 0
  max = 20
  min = -20
  for x in range(1, 13):
    sum += perm_one.log_weight(x, max, min)

  counter = 0
  for x in range(1, 13):
    counter += perm_one.log_weight(x, max, min)
    print counter/sum
  '''
  print "============"

  '''
  # testing shuffle
  for x in range(0, 10):
    print perm_one.shuffle([], [1, 2, 3, 4], [1, 1, 1, 1])
  '''




# testing pref_shuffle
def test_pref_shuffle():
  perm_one = Block(1, 12, "perm")
  print perm_one.pref_shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

def test_pref():
  perm_one = Block(1, 12, "perm")
  print perm_one.pref

#test_block()

for i in range(0, 10):
  test_pref()



