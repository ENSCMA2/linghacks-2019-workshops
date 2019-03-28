from collections import Counter

# variables
myFirstVariable = 5 #int
print(myFirstVariable)
myFirstVariable = 6.7 #float
print(myFirstVariable)
myFirstString = 'this is a string'
print(myFirstString)
myBoolean = (4<5)
print(myBoolean)


# number operations
x = 5
y = 7
y = y+1
y -= 1 # equivalent to y = y - 1, same for +
z = x+y # addition
print('z = ' + str(z))
w = x-y # subtraction
print('w = '+ str(w))
a = w*z # multiplication
print('a = ' + str(a))
b = w/z # division
print('b = ' + str(b))
c = x**y # exponentiation
print('c = ' + str(c)) # convert int to string
d = c//a # floor division
print('d = ' + str(d))
f = d % x # modulo
print('f = ' + str(f))

# boolean logic
myFirstBool = (4 == 5)
mySecondBool = (56*4 < 65*5)
print(myFirstBool)
print(mySecondBool)
print(myFirstBool and mySecondBool)
print(myFirstBool or mySecondBool)
print(not myFirstBool)
myFirstBool = (4 <= 5 and (5 >= 4 or not 6 == 7))
print(myFirstBool)

# lists
myFirstList = [1,2,3,4] # list
print(myFirstList[0]) # first element in list
print(myFirstList[-1]) # last element in list
myFirstList[3] = 5
print(repr(myFirstList))
myFirstList.append(5)
print(repr(myFirstList))


print('last two: ' + repr(myFirstList[3:5]))
print('skipping by twos: ' + repr(myFirstList[0:5:2]))
print('first two: ' + repr(myFirstList[:2]))
print('3rd item onwards: ' + repr(myFirstList[2:]))
myFirstList.insert(3, 6) # index, value
print('insertion: ' + repr(myFirstList))


myFirstList.pop(1)
print('second element popped: ' + repr(myFirstList))
del myFirstList[0]
print('first item deleted: ' + repr(myFirstList))
myFirstList.reverse()
print(repr(myFirstList))
listInList = [[1, 2, 3], [4,5,6],[7,8,9]]
print(listInList[0][1])
print(len(listInList))


# strings
sentence = 'I love natural language processing.'
splitSentence = sentence.split()
print(repr(splitSentence))
sentenceJoinedBackTogether = ' '.join(splitSentence)
print(sentenceJoinedBackTogether)
myMultilineSentence = ''' I really
really love
NLP.'''
print(myMultilineSentence)
mySpecialSentence = 'I\'m so \nspecial \ttoday.'
print(mySpecialSentence)
print(len(mySpecialSentence))

# characters
char1 = 'a'
char2 = 'b'
print("a comes before b:", ord(char1) < ord(char2))

# dictionaries
myFirstDict = {'chocolate': 'yes', 'cheese': 'meh', 'vegetable': 'nope'}
print(myFirstDict)
print(myFirstDict['chocolate'])
myFirstDict['apples'] = 'keep the doctor away'
print(myFirstDict)
del myFirstDict['cheese']
print(myFirstDict)


# counters
myCountingList = ['dog', 'dog', 'cat', 'cat', 'cat', 'fry', 'leopard', 'bread', 'bread']
myFirstCounter = Counter(myCountingList)
print("my first counter: ", myFirstCounter)

# conditional statements
myStatement = (54 < 18*3)
myOtherStatement = (len('yes') == 3)
if(myStatement == False):
  print('myStatement is false!')
elif(myOtherStatement == True):
  print('myOtherStatement is true!')
else:
  print('haha nope')


# contrast elif with if
if(myStatement == False):
  print('myStatement is false!')
if(myOtherStatement == True):
  print('myOtherStatement is true!')
else:
  print('nah')


# try nesting
if(4 > 5):
  if(5 != 5):
    print('nope')
  else:
    print('yep')
else:
  print('welp')

# loops
for i in range(10): # range is the set of integers from 1 to the number inside the parentheses
  print(i)


for number in myFirstList:
  print(number+1)
for i in myFirstDict: # again, time complexity O(n)
  print(i, myFirstDict[i])

# nested for loops
for i in listInList:
  for j in i:
    print(j)


# while loops
n = 6
while n > 0: # time complexity: O(n)
  print('n is positive!')
  n -= 1


# functions
def average(numbers):
  total = 0
  for i in numbers:
    total += i
  return total/len(numbers)

print(average([1,2,3,4,5,6]))

# too hot to handle
slightlyFancyList = [i for i in range(12)]
print(repr(slightlyFancyList))
slightlyFancierList = [i for i in range(12) if i % 2 == 0 and i != 4]
print(repr(slightlyFancierList))
reallyFancyList = [average(i) for i in listInList if average(i) > 3]
print(repr(reallyFancyList))

