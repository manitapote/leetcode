import re

txt = "aaba"

#Check if the string ends with 'planet':

x = re.findall("(\b[a]\b)|(\b[a]([ab]*)[a]\b)|(\b[b]\b)|(\b[b]([ab]*)[b]\b)", txt)
if x:
  print(x)
else:
  print("No match")

# \A, ^ = start of the line, '\Aa', '^a'
# \Z, $ = match end of the line, 'c\Z', 'c$'
# \b match characters at the start and end of the word, \bfox\b
# \B match characters in the middle of other non-space characters
#. anything except for a line break