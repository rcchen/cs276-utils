import cs276

# Single word bigram test
bigrams_word = cs276.ngrams("humpty", 2)
for bigram in ['$h', 'hu', 'um', 'mp', 'pt', 'ty', 'y$']:
  assert bigram in bigrams_word

# Multiple word bigram test
bigrams_words = cs276.ngrams("humpty dumpty", 2)
for bigram in ['$h', 'hu', 'um', 'mp', 'pt', 'ty', 'y$', '$d', 'du', 'um', 'mp', 'pt', 'ty', 'y$']:
  assert bigram in bigrams_words

# Gamma encoding test
assert cs276.encodeGamma(1) == "0"
assert cs276.encodeGamma(4) == "11000"
assert cs276.encodeGamma(24) == "111101000"

# Delta encoding test
assert cs276.encodeDelta(7) == "10011"

# Gamma decoding test
assert cs276.decodeGamma("0")[0] == 1
assert cs276.decodeGamma("111101000")[0] == 24
assert cs276.decodeGamma("110001011000") == [4, 3, 2, 1]
