
# coding: utf-8

# In[128]:

import itertools as iter
import numpy.random as ran

def RSD (initial, preferences):
    agents = []
    pool = []
    order = []
    allocation = []
    for i in range(len(initial)):
        agents.append(initial[i][0])
        pool.append(initial[i][1])
    order = ran.permutation(agents)
    for i in range(len(order)):
        agent_i = order[i]
        preference_i = list(y for x, y in preferences if x == agent_i)[0]
        for j in range(len(preference_i)):
            if preference_i[j] in pool:
                allocation.append((agent_i, preference_i[j]))
                pool.remove(preference_i[j])
                break
    return allocation

final_alloc = []
def IR_RSD (initial, preferences):
    global final_alloc
    alloc = RSD(initial, preferences)
    not_IR = []
    for i in range(len(alloc)):
        agent_i = alloc[i][0]
        allocated = alloc[i][1]
        preference_i = list(y for x, y in preferences if x == agent_i)[0]
        initial_i = list(y for x, y in initial if x == agent_i)[0]
        if preference_i.index(initial_i) < preference_i.index(allocated):
            not_IR.append(agent_i)
    if len(not_IR) == 0:
        final_alloc = final_alloc + alloc
        return final_alloc
    else:
        cut = ran.choice(not_IR)
        final_alloc = final_alloc + (list(x for x in initial if x[0] == cut))
        initial = list(x for x in initial if x[0] <> cut)
        return IR_RSD(initial, preferences)

print(RSD([(1,1),(2,2),(3,3)],[(1, [1, 2, 3]), (2, [2, 1, 3]),(3,[3, 2, 1])]))
print(IR_RSD([(1,1),(2,2),(3,3)],[(1, [3, 2, 1]), (2, [3, 1, 2]),(3,[3, 2, 1])]))

def welfare_calc(allocation, preferences):
    

a = iter.permutations([1, 2, 3])
list(a)


# In[62]:

"""implement utility function?"""


# In[ ]:



