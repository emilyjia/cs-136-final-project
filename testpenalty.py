from block import Block

'''
unit tests for the penalty function
'''

def test_penalty():
  index = [0,0,0,0,0,0,0,0,0,0,0, 0]
  for x in range(0, 1000):
    block = Block(1, 12, "perm")
    pref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    result = block.log_penalty(pref, 4)
    for i in range(0, 12):
      index[result[i]-1]+=i+1
  print [x/1000.0 for x in index]

test_penalty()

