# Demo:  python3 xample.py
from cli import cli

def ageAndShoeSize(
        dob: "date of birth" = 1960,
        elated: "make happy" = False,
        where: "birth place" = ["nsw", "vic"],
        shoes: "shoesize" = 10):
  """Good times for all.
  (c) Tim here now 2021"""
  print(f"{where} dob + shoes = {dob+shoes} elated= {elated}")

if __name__ == "__main__": 
  cli(ageAndShoeSize)
