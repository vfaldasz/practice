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
    """Write a method to replace all spaces in a string with '%20.'"""
    return string.replace(" ", "%20")
string= "Mr John Smith    "
#print(make_url(string))



def make_url2(string):
    letters = list(string)
    i = len(letters) - 1
    print (i)
    j = i
    print (j)
    while letters[i] == " ":
        i -= 1
    print (i)
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




