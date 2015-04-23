### Usage

To use the cs276 library, simply place it in the same directory as your scripts and call `import cs276`

`ngrams(s,n)` - returns a list of all n-grams for a string. Beginnings and ends of words are indicated with a $, and strings are split into words with a space as the delimiter.

`permuterms(s)` - returns a list of all permuterms for a string. String is split into words with a space as the delimiter. Each word is augmented with a $.

`encodeGamma(n)` - returns the Gamma encoding for a number.

`decodeGamma(s)` - returns a list of numbers decoded from a Gamma encoded string.

`encodeDelta(n)` - returns the Delta encoding for a number.
