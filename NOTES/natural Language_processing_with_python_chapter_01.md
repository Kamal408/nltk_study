## Natural Language Processing with Python, Chapter 1

 1. Installation of texts
 
        from nltk.book import *

 1. Methods encountered

   * **nltk.text.Text.concordance(str, lines=25)**: concordance of examples
   * **nltk.text.Text.similar(str, num=20)**: distributional similarity
   * **nltk.text.Text.common_contexts(list, num=20)**: Find contexts where the specified words appear; list most frequent common contexts first.
   * **nltk.text.Text.dispersion_plot(list, num=20)**: Produce a plot showing the distribution of the words through the text.
   * **generate(length=100)**: Print random text, generated using a trigram language model.


[end]