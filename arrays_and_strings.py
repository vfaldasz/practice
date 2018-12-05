def is_unique(string):
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
    for char in string:
        print (char)
        counter = unique.get(char, 0)+1
        print (counter)
        if counter > 1:
            return False
    return True

string = "asdifFfffff"
#print (is_unique(string))

