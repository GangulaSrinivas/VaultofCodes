def count_words(text):
  """Counts the frequencies of words in a given text."""
  words = text.split()
  word_counts = {}
  for word in words:
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1
  return word_counts
text = "This is a sample text. It contains some words."
word_counts = count_words(text)
print(word_counts)
