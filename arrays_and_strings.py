def is_unique(string):
"""1.1 Implement an algorithm to determine if a string has all unique characters."""
    unique = []
    for char in string:
        if char in unique:
            return False
        else:
            unique.append(char)
    return True

string = "asdifF"
print (is_unique(string))




def is_unique(string):
    unique = {}
    for letter in string:
        counter = unique.get(letter, 0)+1
        unique[letter]= counter 
        if counter > 1:
            return False
    return True

string = "asdifzFffff"
print (is_unique(string))




def is_unique(string):
"""Solve problem without data structures. Runtime is n^2"""
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False

    return True
string= "pqqrz"
print(is_unique(string))





def is_permutation(string1, string2):
"""1.2 Given two strings, write a method to decide if one is a permutation of the other."""
    dict1 = {}
    dict2 = {}
    for letter in string1:
        value = dict1.get('letter', 0)+1
        dict1['letter']=value
    for letter in string2:
        value = dict2.get('letter', 0)+1
        dict2['letter']=value
    for item in dict1.items():
        if item in dict2.items():
            return True
    return False


string1= 'odor'
string2= 'door'
print(is_permutation(string1, string2))




def make_url(string):
    """1.3 Write a method to replace all spaces in a string with '%20.'"""
    return string.replace(" ", "%20")
string= "Mr John Smith    "
print(make_url(string))




def make_url2(string):
    letters = list(string)
    i = len(letters) - 1
    j = i
   
    while letters[i] == " ":
        i -= 1
   
    while j != i:
        if letters[i] == " ":
            letters[j-2] = "%"
            letters[j-1] = "2"
            letters[j]   = "0"
            j -= 2
        else:
            letters[j] = letters[i]
        i -= 1
        j -= 1
    return ''.join(letters)

string= "Mr John Smith    "
print(make_url2(string))




def perm_of_palindrome(string):
    """ 1.4 Given a string, determine if it is a permutation of a palindrome"""

  dict={}

  for letter in string:
    value =dict.get(letter, 0)+1
    dict[letter]= value

  counter = 0
  for value in dict.values(): 
    if value % 2 == 1: #if values is evenly divisible by 2, then we know its a palindrome. We can allow for only one odd value (i.e in radar 'd' is your odd value.  However, radars (d and s is your odd value, therefore it would not be a palindromee))
      counter +=1
    if counter > 1:
      return False

  return True

string = "tacocat"

print(perm_of_palindrome(string))




def sum_of_unique_nums(x,y):
    for item in x:
        if item not in y:
            y.append(item)
    print (y)
    #return y 
    
    result= 0
    for item in y:
        result= result + item
    return result 

n= [2,4,4,6,8,8]
m= []
#print (sum_of_unique_nums(n,m))



def one_away(str1, str2):
# Determine whether the edit distance between two strings is less than 2.
  len_diff = abs(len(str1) - len(str2))
  if len_diff > 1:
    return False
  elif len_diff == 0:
    difference_count = 0
    for i in xrange(len(str1)):
      if str1[i] != str2[i]:
        difference_count += 1
        if difference_count > 1:
          return False
    return True
  else:
    if len(str1) > len(str2):
      longer, shorter = str1, str2
    else:
      longer, shorter = str2, str1
    shift = 0
    for i in xrange(len(shorter)):
      if shorter[i] != longer[i + shift]:
        if shift or (shorter[i] != longer[i + 1]):
          return False
        shift = 1
    return True

# Write a function that takes in 3 integers as arguments and returns a list of numbers from 1 to 100 (inclusive), containing only integers that are evenly divisible by at least one of the integers.
# For example, given 50, 30, and 29, return [29, 30, 50, 58, 60, 87, 90, 100].

def divisible(x,y,z):
    num = 1
    a=[]
    while num<101:
        if (num % x == 0) or (num % y == 0) or (num % z == 0):
            a.append(num)
        num +=1
    return a


l= 50
m= 30
n= 29
#print (divisible(l,m,n))



