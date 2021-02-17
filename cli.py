#i!/usr/bin/env python3
# vim: ts=2 sw=2 sts=2 et tw=81:
"""
Succinct CLI tool that uses from function name, docstring, and default args.   
(c) 2021 Tim Menzies <timm@ieee.org>, MIT License

Example usage:

    from cli import cli
    def ageAndShoeSize(
            dob:    "date of birth" = 1960,
            elated: "make happy"    = False,
            where:  "birth place"   = ["nsw", "vic"],
            shoes:  "shoesize"      = 10):
      "Good times for all.  (c) Tim here now 2021"
      print(f"{where} dob + shoes = {dob+shoes} elated= {elated}")
    
    if __name__ == "__main__": 
      cli(ageAndShoeSize)

"""
import inspect
import argparse as arg

def cli(f):
  "Call `f`, first checking if any command line options override the defaults."
  do = arg.ArgumentParser(
          prog            = f.__name__,
          description     = (f.__doc__ or '').split("\n\n")[0],
          formatter_class = arg.RawDescriptionHelpFormatter)
  for key, v in inspect.signature(f).parameters.items():
    do.add_argument("-"+key, 
                    **details(v.default, v.annotation))
  return f(**vars(do.parse_args())) 

def details(x,txt,choices=None):
  "Find the help text, defaults, return types withn `x`."
  isa= isinstance
  if isa(x, list): 
    return details(x[0], txt, choices=x)
  m, t = (("I", int)   if isa(x, int)   else (
          ("F", float) if isa(x, float) else ("S", str)))
  h = f"{txt}; default= {x} " + (f"range= {choices}" if choices else "")
  if choices: 
    return dict(help=h, default=x, metavar=m, type=t, choices=choices)
  if x is False: 
    return dict(help=h, action='store_true')
  else:
    return dict(help=h, default=x, metavar=m, type=t)


