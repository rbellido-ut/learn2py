#!/usr/bin/python2.7 -tt

import sys

def Hello(name):
   if name == 'Alice' or name == 'Nick':
      name = name + '???'
   else:
      DoesNotExist(name)
   name = name + '!!!!'
   print 'Hello', name

# define a main() function that prints a little greeting
def main():
   Hello(sys.argv[1])

# This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
   main()
