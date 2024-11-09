"""
Write a function which takes two string arguments.
The function should combine the strings using the 
largest overlap they share - the ending of the 
first string should overlap the beginning of the second.

"""

def overlap(a,b):
    x = a + b
    doubled_letters = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            doubled_letters = doubled_letters + a[i]
        print(doubled_letters)
    print(x.replace(doubled_letters,""))


overlap("abcde","cdefgh")