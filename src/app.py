import nltk

# nltk.download("tagsets")

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

example_string = """All we have to decide is what to do with the time that is given to us.
There are other forces at work in this world, Frodo, besides the will of evil."""

#
# Tokenization
# Tokenization is the process of breaking a stream of text up into words, phrases, symbols, or other meaningful elements called tokens.
#

# Stopwords are the words that are filtered out before or after processing of natural language data.
stop_words = set(stopwords.words("english"))

# Tokenize by sentences
sentences = sent_tokenize(example_string)

# Tokenize by words
words = word_tokenize(example_string)

# Filtering based on the english stopwords.
# This filtering, is actually remove I and Not words, those are important sometimes, so keep that in mind.
filtered_words = [word for word in words if word.casefold() not in stop_words]

print("Filtered")
print(filtered_words)

#
# Stemming
# Stemming is the process of reducing inflected (or sometimes derived) words to their stem, base or root form.
#

stemmer = SnowballStemmer("english")
stemmed_words = [stemmer.stem(filtered_word) for filtered_word in filtered_words]

print("\nStemmed words")
print(stemmed_words)

#
# Tagging Parts of Speech
# Tagging is the process of marking up a word in a text (corpus) as corresponding to a particular part of speech,
# based on both its definition and its context.
#

# nltk.help.upenn_tagset()
pos_tag = nltk.pos_tag(stemmed_words)

print("\nParts of Speech array")
print(pos_tag)

#
# Lemmatizing
# Lemmatization is the process of grouping together the inflected forms of a word so they can be analysed as a single item.
#

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

print("\nLemmatized words")
print(lemmatized_words)

# print("\nLemmatized the word worst, example case")
# # treated as noun by adding the parameter, default behavior
# print(lemmatizer.lemmatize("worst"))
# # treated as an adjective by adding the parameter
# print(lemmatizer.lemmatize("worst", pos="a"))

#
# Chunking
# Chunking is the process of extracting phrases from unstructured text.
# This is a complementary process for the tokenization. You basically chunks by phrases.
#

# We start by tokenizing the string and then tagging the words with parts of speech.
lotr_quote = "It's a dangerous business, Frodo, going out your door."
words_in_lotr_quote = word_tokenize(lotr_quote)
lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)

# print("\nlotr_pos_tags")
# print(lotr_pos_tags)

# Now, we create a chunk grammar, which is a combination of rules on how sentences should be chunked.
# It often uses regular expressions, or regexes.

# The following grammar will:
# Start with an optional (?) determiner ('DT')
# Can have any number (*) of adjectives (JJ)
# End with a noun (<NN>)

grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(lotr_pos_tags)
tree.draw()
