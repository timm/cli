Module clink
============
Succinct CLI tool that uses from function name, docstring, and default args.   
License: (c) 2021 Tim Menzies <timm@ieee.org>, MIT License  
Doco: http://menzies.us/clink   
Code: http://github.com/timm/clink

Example:

Functions
---------

    
`ageAndShoeSize(dob: date of birth = 1960, elated: make happy = False, where: birth place = ['nsw', 'vic'], shoes: shoesize = 10)`
:   Demo of clink:
    Function args args annotated with defaults and help text.
    Users can overide the defautsl in a command line-inferface using
    
      __name__=="__main__" and clink(ageAndShoeSize)

    
`clink(f)`
:   Call `f`, first checking if any command line options override the defaults.

    
`details(x, txt, choices=None)`
:   Find the help text, defaults, return types withn `x`.
