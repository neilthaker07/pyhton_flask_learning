#unpack list , tuples
no1,no2,no3, y = ['a','b','c',81]

print no1
'''
def grades(gra):
	first, *mid, last = gra  # list objects division
	print sum(mid)/len(,mid)
grades([10,11,12,13,14])
'''
#zip
names = ['abc','def','ghi']
last = ['p','q','r']

nn = zip(names,last)
print nn

#lambda
answer = lambda x: x*7
print answer(5)

stock = {
	'A': 100,
	'B': 50,
	'C':75
}
# sort dictionary
print min(zip(stock.values(),stock.keys()))   # sorting or min or max by zip functionality and in that first ARGUMENT
print max(zip(stock.values(),stock.keys()))
print sorted(zip(stock.values(),stock.keys()))

# pillow
# map
income = [150, 200, 120, 600]

def check(dollars):
	return dollars * 2

print map(check, income)

# bitwise operator
a = 50 		# 110010
b = 25 		# 011001 
c = a & b   # 010000   Binary AND

print c

print c >> 2 # right shift 2 spots   000100

# find largest or smallest
import heapq
grades = [25,10,62,55,90,88]
print heapq.nlargest(3, grades)
print heapq.nsmallest(1, stock, key=lambda sto: sto)  # use key to sort specifically

print min(stock) # keywise sorting

minprice = min(zip(stock.values(), stock.keys()))
print minprice

# most frequent items in list
text = "Hello how are you. This is from web. This is very good. Learn Learn Testing. Hello How to do testing"
from collections import Counter

words = text.split()
print words
counter = Counter(words)
print counter
print counter.most_common(5) # most common five words

# dictionary sorting
from operator import itemgetter
users = [
	{'name':'z','no':1},
	{'name':'r','no':4},
	{'name':'q','no':9},
	{'name':'t','no':3},
	{'name':'q','no':2}
]

for x in sorted(users, key=itemgetter('name')):
	print x	

print '-----------'
for x in sorted(users, key=itemgetter('name','no')):
	print x

from operator import attrgetter

class User:
	def __init__(self,x,y):
		self.name = x
		self.userid = y
		
	def __repr__(self):
		return self.name + ' : ' + str(self.userid)
		
users=[
	User('Buc','9'),
	User('Abc','5'),
	User('pu','7')
]

for user in users:
	print user
	
print '-------------------'

for user in sorted(users, key=attrgetter('name')):   # class object name
	print user













