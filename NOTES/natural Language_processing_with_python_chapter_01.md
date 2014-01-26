## Natural Language Processing with Python, Chapter 1

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

 1. Classes encountered

   * **class nltk.probability.FreqDist()**: records the number of times each outcome of an experiment has occurred

 1. Structure of texts
 
 They are lists of words and tokens.

 1. Terms and measures of texts
 
   * **[word] types**: unique forms of words or other entities such as punctuation
   * **lexical diversity**: (total words) / (unique words)



[end]