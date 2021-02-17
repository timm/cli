import inspect
import argparse as arg

def cli(f):
  "Call `f`, first checking if any command line options override the defaults."
 #----------------------------------------------------
  do = arg.ArgumentParser(
          prog            = f.__name__,
          description     = (f.__doc__ or '').split("\n\n")[0],
          formatter_class = arg.RawDescriptionHelpFormatter)
  for key, v in inspect.signature(f).parameters.items():
    do.add_argument("-"+key, 
                    **_details(v.default, v.annotation))
  return f(**vars(do.parse_args())) 

def _details(x,txt,choices=None):
  isa= isinstance
  if isa(x, list): 
    return _details(x[0], txt, choices=x)
  m, t = (("I", int)   if isa(x, int)   else (
          ("F", float) if isa(x, float) else ("S", str)))
  h = f"{txt}; default= {x} " + (f"range= {choices}" if choices else "")
  if choices: 
    return dict(help=h, default=x, metavar=m, type=t, choices=choices)
  if x is False: 
    return dict(help=h, action='store_true')
  else:
    return dict(help=h, default=x, metavar=m, type=t)


