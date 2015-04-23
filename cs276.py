import math

# Retrieves a list of all ngrams for a string
# Beginnings and ends of words are indicated with a $
# Strings are split into words with spaces as a delimiter
def ngrams(s, n):
  grams = []
  for word in s.split(" "):
    for i, c in enumerate(word):
      if i == 0:
        grams.append("$" + word[:i+n-1])
      if i > len(word) - n:
        grams.append(word[i:] + "$")
        break
      grams.append(word[i:i+n])
  return grams

# Generates a list of permuterms for a string
# Terms are augmented with a $ and then rotated through all positions
# Strings are split into words with spaces as a delimiter
def permuterms(s):
  terms = []
  for word in s.split(" "):
    amended = word + "$"
    for _ in xrange(len(amended)):
      rotation = amended[-1] + amended[:-1]
      terms.append(rotation)
      amended = rotation
  return terms

# Converts a number into gamma encoding
def encodeGamma(n):
  length = ["1" for _ in xrange(int(math.floor(math.log(n, 2))))]
  offset = bin(n)[3:]
  return ("").join(length) + "0" + offset

# Converts a number into delta encoding
def encodeDelta(n):
  length = encodeGamma(int(math.floor(math.log(n, 2))))
  offset = bin(n)[3:]
  return ("").join(length) + offset

# Converts a gamma encoding(s) into a list of numbers
def decodeGamma(s):
  results = []
  while len(s) > 0:
    length = s.index('0')
    offset = s[length+1:length*2+1]
    results.append(int("1" + offset, 2))
    s = s[length*2+1:]
  return results

# Converts a delta encoding into number
def decodeDelta(s):
  return s
