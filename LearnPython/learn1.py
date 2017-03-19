print 2 ** 3
print 'hi'
fname = 'abcdefgh'
print fname[-1]  #from last char is negative sign 
print fname[3:]
print len('hhh')

print 'neil'+'thaker',999
#     + is for same data types and    , is for different data types contanatenation

players = [15, 20 ,16]
print players[0]  
players + [99,91]   #here players list is not going to change
players.append(61) # only one item per append
print players
players[:1]=[]  # remove item from list
print players

age = 20
if age is 10:
	print 'yyeess'
elif age == 20:
	print 'hmm'
else:
	print 'nnoo'
	
nos = ['a','b','c']
for i in nos:
	print i

for j in range(5):
	print j


def test(i=1):
	r = i,'inside function'
	return r

r = test(11)
r1 = test(22)
r3 = test()
print("start ",r," end",r1, r3)

def t3(*a): # flexible number of arguments
	total = 0
	for i in a:
		total = total + i;
	print total

t3(4)
t3(4,5,6)

def unpack1(a,b,c):
	print a+b+c;
	
unpack_use = [1,2,3]
unpack1(*unpack_use)

#sets no duplicates - in curly braces
grocery = {'ab','cd', 'ab'}
print grocery

#dictionary - key and values
classmates = {'k1':1,'k2':2}
print classmates['k1']

for k,v in classmates.items():
	print k , " " , v
	
# modules	
import funtest

funtest.fish()
# random number generator function
import random
x = random.randrange(1,100)
print x
'''
fw = open('sample.txt', 'w') # write
fw.write('fisttesting in file from python')
fw.close()
'''
fr = open('sample.txt','r') # read
data = fr.read()
print data
fr.close()
'''
# import module from web
from urllib import request
weburl = 'www.google.com'

def downloaddata(csvurl):
	response = request.urlopen(csvurl)
	cc = str(response.read())
	
downloaddata(weburl)
'''
# exception
while True:
	try:
		ip = int(input('what'))
		print ip
		break
	except:
		print 'in exception'
		break
	finally:
		print 'in finally'

#class and objects
class First:
	life = 3
	
	def attack(self):
		print self.life - 1 , 'oo'

	def chk(self):
		print self.life , 'this is life'
	
first = First()

first.attack()
first.chk()

# init , instance variable

class Tune:
	common = 'hi' # class var
	def __init__(self, x): # instantiation , intialize - this executes every time in the class like constructor
		print 'inside init'  # x is instance var - local var
		self.getit = x
	def normal(self):
		print 'in normal' , self.getit

tune = Tune(4)
tune1 = Tune(5)
tune.normal()
print(tune.common)
print(tune1.common)

#inheritance
class Parent:
	def name(self):
		print 'parent'

class Parent2:
	def name2(self):
		print 'parent2'

class Child(Parent, Parent2):
	def no(self):
		print 'child'

	def name(self):  # function overriding
		print 'overriding'

p = Child()
p.no()
p.name()
p.name2()

#threading
import threading
class testthread(threading.Thread):
	def run(self):  # inbuuilt run method
		for _ in range(10):
			print threading.currentThread().getName()
					
tt = testthread(name='sending')
tt2 = testthread(name='receiving')

tt.start()  # start a thread, thread runs parallel
tt2.start()		
		
		
		







