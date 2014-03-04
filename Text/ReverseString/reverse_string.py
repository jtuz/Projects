#coding: utf-8
"""
Reverse a string - Enter a string and the program
will reverse the string and print out.
"""

if __name__ == '__main__':

    # Prompt to the user for the string
    string = raw_input("Please, ingress a string to invert: ")

    # Invert the string using slice syntax [begin:end:step]
    reversed_string = string[::-1]

    print "The string %s reversed is %s" % (string, reversed_string)
