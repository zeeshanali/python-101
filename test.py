""" this is my first program
    so i am kind of enjoying
    learning CS to serve Islam
"""

def is_sahaba(x,y):
    if x in y:
        return True
    else:
        return False


a = "Assalamo Alaikum" + "waremutllah barakatuthu"

c = "%s loves %s" % ("I", "Allah")

b = "{who} loves {whome}".format(who="I", whome="Allah")

print a
print b

print (c)


#http://stackoverflow.com/questions/509211/explain-pythons-slice-notation

"""
a[start:end] # items start through end-1
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through end-1
a[:]         # a copy of the whole array
There is also the step value, which can be used with any of the above:

a[start:end:step] # start through not past end, by step
The key point to remember is that the :end value represents the first value that is not in the selected slice. So, the difference beween end and start is the number of elements selected (if step is 1, the default).

The other feature is that start or end may be a negative number, which means it counts from the end of the array instead of the beginning. So:

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
Python is kind to the programmer if there are fewer items than you ask for. For example, if you ask for a[:-2] and a only contains one element, you get an empty list instead of an error. Sometimes you would prefer the error, so you have to be aware that this may happen.

"""


list_sahabas = ["Khadija","Abu Bakr", "Ali", "Usman", "Umar"]


print (list_sahabas[1::2])
print (list_sahabas[2:3])

print ("Khadija" in list_sahabas)


surah_dictionary = {"Fatiha":"Makki", "Baqra":"Madni"}

print surah_dictionary["Fatiha"]

s = "Ali"

print surah_dictionary.get(s)

"""
The error explains that you cannot perform string concatenation of a string ('_') and an object which value is None. It means at this point self.name is None, so you need to trace where self.name is being defined, and if you are storing the value correctly
If you still want to concatenate the two values, consider using string formatting instead of the '+' sign.
eg return '_%s' % self.name would return '_None' if self.name value is None

"""
print " is  " + s + "   in Sahab %s " % surah_dictionary.get(s)

list_sahabas.append("Aisha")


if s in list_sahabas :
    print "yes"
else:
    print "no"

print(" Now check via function %s " % is_sahaba("Ali",list_sahabas) )

"""for sahaba in list_sahabas:
    print (" %s is Sahaba" %sahaba)
"""

"""for i in range(4):
    print i
"""

"""
The *args and **kwargs is a common idiom to allow arbitrary number of arguments to functions as described in the section more on defining functions in the Python documentation.
The *args will give you all function parameters as a tuple:
"""


"""
first class functions , need for functional programming
return function as value

"""
def add1(x):
    def add2(y):
        return x+y
    return add2

add10=add1(2)

print add10(4)






















