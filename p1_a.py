#Group 3
#TEAM MEMBERS: [Jennifer ly,
#CSC 495 DATA MINING
#project 1

# FUNCTION SET

from fractions import Fraction
from itertools import permutations


def powerset(A):
    A = (list(filter(lambda a: a != 0, A)))
    if A == []:
        return [[]]

    a = A[0]
    incomplete_pset = powerset(A[1:])
    rest = []
    for set in incomplete_pset:
        rest.append([a] + set)
    return rest + incomplete_pset


#cleans up  the resulting powerset and drops any sublist that is greater than the largest transaction
def powerlist(flat_db, maxtrans):
    pl = (powerset(flat_db))
    pl = [y for y in pl if y != []]
    pl = sorted(([z for z in pl if len(z) < maxtrans]), key = lambda l: (len(l),1))
    return pl

#helper function for association rules
# 1. first find how many times X happened in the original DB
# 2. From 1, how many times does Y happened
# 3. Returns confidence values

def search(DB, X, Y,mc):
    xct, yct = 0,0
    alist = []
    #print(X,Y)
    for item in DB:
        #print(set(X).issubset(set(item)))
        if set(X).issubset(set(item)):
           xct = xct + 1
           alist.append(item)
  #  print(alist)
    for a in alist:
        if set(Y).issubset(set(a)):
            yct = yct + 1
    if (yct/xct) >= mc :
        return  (yct/xct)
    if (yct/xct) < mc:
        return 0

# compares each list from the powerset list and tests if it's subset of a transaction from DB
# if the the sublist has a support value >= minconf, print the sublist and support value
# returns frequency itemset to forward over for association rules
def apriori_alg(DB, PS, minsup):
    freq_i_set = list()
    ctr = 0
    for y in PS:
        for x in DB:
          if set(y).issubset(set(x)):
            ctr = ctr + 1
        ratio = ctr/len(DB)
        if ratio >= minsup:
            freq_i_set.append(list(y))
            print(ratio, y)
        ratio,ctr = 0,0
    return freq_i_set,


# any list of length 1 in frequency list is dropped, as you cannot make a rule with that
# remaining lists are expanded to create all possible permutations
# depending on the size of the list, split the list elements to 2 parts to generate X -> Y confidence values
# actual calcuations are done in the helper functino: SEARCH

def AR (freqset, minconf,db_in):

    freq_list = sorted(([z for z in freqset if len(z) > 1 ]), key=lambda l: (len(l), 1))
    b =[]
    #create the lists
    for x in freq_list:
        l = list(permutations(x))
        l = list(map(list, l))
        b.append(l)

    for x in b:
        for y in x:
            if len(y) == 2:
                first,second = [],[]
                first.append(y[0])
                second.append(y[1])
              #  print(first, second)
                conf = (search(db_in, first, second,minconf))
                if conf >= minconf:
                    print(first,'--->', second, ' with a confidence of ', conf)
            if len(y) > 2:
                ctr = 0
                for yitem in y:
                    ctr = ctr + 1
                    first = y[:ctr]
                    if len(first) < len(y):
                        second = y[ctr:]
                        conf = (search(db_in, first, second, minconf))
                        if conf >= minconf:
                            print(first, '--->', second, ' with a confidence of ', conf)
