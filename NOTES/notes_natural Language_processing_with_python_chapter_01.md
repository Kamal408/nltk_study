## Notes, Natural Language Processing with Python, Chapter 1

 1. Installation of texts
 
        from nltk.book import *

 1. Methods encountered

   * **nltk.text.Text.concordance(str, lines=25)**: concordance of examples
   * **nltk.text.Text.similar(str, num=20)**: distributional similarity
   * **nltk.text.Text.common_contexts(list, num=20)**: Find contexts where the specified words appear; list most frequent common contexts first.
   * **nltk.text.Text.dispersion_plot(list, num=20)**: Produce a plot showing the distribution of the words through the text.
   * **nltk.text.Text.generate(length=100)**: Print random text, generated using a trigram language model.
   * **nltk.text.Text.count(str)**: Count the number of times this word appears in the text.
   * **nltk.text.Text.index(str)**: Find the index of the first occurrence of the word in the text.
   * **nltk.text.Text.collocations(self, num=20, window_size=2)**: Print collocations derived from the text, ignoring stopwords.
   * **nltk.util.bigrams(sequence, **kwargs)**: Return a sequence of bigrams from a sequence of items.
   * ****: 
   * ****: 
   * ****: 

 1. Classes encountered

   * **class nltk.probability.FreqDist(text)**: records the number of times each outcome of an experiment has occurred. Some of the methods:

     1. `items()`: Return list of (key, value) tuples.
     1. `freq(sample)`: Return the frequency of a given sample.
     1. `plot(*args, **kwargs)`: Plot samples from the frequency distribution. If two integer parameters m, n are supplied, plot a subset of the samples, beginning with m and stopping at n-1.
     1. `B()`: Return the total number of sample values (or "bins") that have counts greater than zero.
     1. `N()`: Return the total number of sample outcomes that have been recorded by this FreqDist
     1. `Nr(r, bins=None)`: Return the number of samples with count r.

 1. Structure of texts
 
 They are lists of words and tokens.

 1. Terms and measures of texts
 
   * **[word] types**: unique forms of words or other entities such as punctuation
   * **lexical diversity**: (total words) / (unique words)

[end]