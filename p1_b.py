
# DATA MINING
# project 1

# Test case

from fractions import Fraction
import numpy as np
import pandas as pd

from p1_a import *
# smaller test case to verify calculations were done properly
db_in = [
    ['bread', 'milk'],
    ['bread', 'diaper', 'beer', 'eggs'],
    ['milk', 'diaper', 'beer', 'coke'],
    ['bread', 'milk', 'diaper', 'beer'],
    ['bread', 'milk', 'diaper', 'coke']
]

db_1 = [
    ['sunflower', 'bellflower'], ['rose', 'tulips', 'peonies'],
    ['tulips', 'peonies', 'sunflower', 'bellflower', 'dahlia' ,'marigold'], ['dahlia' ,'marigold', 'daisy', 'violet'],
    ['rose'],
    ['rose', 'tulips'], ['rose', 'dahlia', 'marigold', 'daisy'], ['sunflower', 'bellflower'],
    ['bellflower', 'dahlia', 'marigold', 'daisy', 'violet'], ['rose', 'tulips', 'peonies'],
    ['rose', 'tulips'], ['rose', 'marigold', 'daisy', 'violet'], ['sunflower', 'violet', 'daisy'], ['dahlia', 'daisy'],
    ['marigold', 'daisy', 'violet'],
    ['rose', 'daisy', 'violet'], ['sunflower', 'bellflower', 'dahlia', 'marigold'], ['tulips'], ['rose', 'marigold'],
    ['rose', 'tulips', 'peonies', 'sunflower', 'bellflower', 'dahlia', 'marigold', 'daisy'],

]
db_2 = [
    ['bread', 'milk'], ['beer', 'eggs', 'coke', 'towels', 'pizza'], ['beer', 'pizza'],
    ['bread', 'milk', 'beer', 'eggs', 'coke', 'towels', 'pizza'],
    ['bread', 'diaper', 'beer', 'eggs'], ['towels', 'pizza', 'bread', 'milk'], ['pizza', 'coke'], ['coke'],
    ['milk', 'diaper', 'beer', 'coke'], ['milk', 'beer','coke'], ['pizza', 'coke', 'beer'], ['diaper', 'pizza', 'beer'],
    ['bread', 'milk', 'diaper', 'beer'], ['bread', 'beer'], ['beer', 'milk'], ['beer', 'milk', 'coke'],
    ['bread', 'milk', 'diaper', 'coke'], ['beer','milk'], ['towels', 'diaper','beer'], ['milk','eggs']
]
db_3 = [
    ['house coffee'], ['latte', 'sandwich'], ['juice', 'salad'], ['tea', 'house coffee','juice'],
    ['house coffee', 'sandwich'], ['latte', 'pastry'], ['house coffee', 'tea'], ['tea', 'pastry'],
    ['house coffee', 'sandwich', 'pastry', 'salad','juice'], ['latte', 'sandwich', 'pastry', 'salad', 'mocha', 'juice'],
    ['salad', 'mocha', 'juice'], ['house coffee', 'tea', 'latte'],
    ['house coffee', 'salad', 'mocha', 'juice'], ['tea', 'latte', 'sandwich', 'juice','pastry', 'salad'],
    ['mocha', 'juice', 'tea', 'latte', 'sandwich'], ['salad', 'mocha', 'tea'],
    ['house coffee', 'tea', 'latte', 'sandwich', 'pastry', 'salad', 'mocha'], ['tea', 'latte', 'sandwich'],
    ['sandwich', 'salad'], ['pastry', 'sandwich', 'salad', 'juice']
]

dbflat = list(set([item for sublist in db_in for item in sublist]))

# gets all the unique items in the transactions to then generate powerset
db1_flat = list(set([item for sublist in db_1 for item in sublist]))
db2_flat = list(set([item for sublist in db_2 for item in sublist]))
db3_flat = list(set([item for sublist in db_3 for item in sublist]))

max_test = max(len(x) for x in db_in)

# gets the length of the biggest transaction
# to be used to help trim off going through the entire power set
max1 = max(len(x) for x in db_1)
max2 = max(len(x) for x in db_2)
max3 = max(len(x) for x in db_3)

# generate powerset lists from the given db
pl = powerlist(dbflat, max_test)
pl1 = powerlist(db1_flat, max1)
pl2 = powerlist(db2_flat, max2)
pl3 = powerlist(db3_flat, max3)

# verifier = AR(apriori_alg(db_in,pl, .4)[0], .5 ,db_in)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('FOR DATABASE 1, size:', len(db_1), 'and contains:', len(db1_flat), 'elements')
print(pd.DataFrame((db_1)))

minsup = Fraction((input('Enter in your minsup threshold value: ')))
minconf = Fraction(input('Enter in your minconf threshold value: '))
res_1 = AR(apriori_alg(db_1, pl1, minsup)[0], minconf, db_1)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('FOR DATABASE 2, size:', len(db_2), 'and contains:', len(db2_flat), 'elements')
print(pd.DataFrame((db_2)))

minsup2 = Fraction((input('Enter in your minsup threshold value: ')))
minconf2 = Fraction(input('Enter in your minconf threshold value: '))

res_2 = AR(apriori_alg(db_2, pl2, minsup2)[0], minconf2, db_2)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('FOR DATABASE 3, size:', len(db_3), 'and contains:', len(db3_flat), 'elements')
print(pd.DataFrame((db_3)))

minsup3 = Fraction((input('Enter in your minsup threshold value: ')))
minconf3 = Fraction(input('Enter in your minconf threshold value: '))
res_3 = AR(apriori_alg(db_3, pl3, minsup3)[0], minconf3, db_3)

