def letterPermutations(lettersin):
  import math
  dict = {}
  i = ""
  divider = 1
  lettersin = str(lettersin)
  for i in lettersin.lower():
    if i in dict:
      dict[i] += 1
    else:
      dict.update({i : 1})
     
  for i in dict:
    divider *= math.factorial(dict[i])
  return math.factorial(len(lettersin))/(divider)


print(letterPermutations(input("input letters: ")))
