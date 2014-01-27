## Exercises, Natural Language Processing with Python, Chapter 1

 * 4: How many words are there in text2?

   **Answer**: 

        In [1]: len(text2)
        Out[1]: 141576

   How many distinct words are there?

   **Answer**: 

        In [2]: len(set(text2))
        Out[2]: 6833

 * 6: Produce a dispersion plot of the four main protagonists in Sense and Sensibility: Elinor, Marianne, Edward, and Willoughby. What can you observe about the different roles played by the males and females in this novel? Can you identify the couples?

   **Answer**: 

        text2.dispersion_plot(['Elinor', 'Marianne', 'Edward', 'Willoughby'])

   The female characters appear much more than the male.

   Couples are hard to make out. But Edward and Willoughby seem to appear in alternation!

 * 7: Find the collocations in text5.

   **Answer**: 

        text5.collocations()

 * 15: Find all words in the Chat Corpus (text5) starting with the letter b. Show them in alphabetical order.

   **Answer**: 

        sorted(set([i for i in text5 if i.startswith('b')]))

or

        sorted(set([i for i in text5 if i and i[0] == 'b']))

 * 17: Use text9.index() to find the index of the word sunset. You’ll need to insert this word as an argument between the parentheses. By a process of trial and error, find the slice for the complete sentence that contains this word.

   **Answer**: 

        index = text9.index('sunset')
        start = index
        stop = index
        while True:
            start -= 1
            if start >= 0 and text9[start] == '.':
                start += 1
                break
        while True:
            stop += 1
            if stop < len(text9) and text9[stop] == '.':
                stop += 1
                break
        print 'text9[{}:{}]: {}'.format(start, stop, text9[start:stop])

 Output: 

        text9[613:644]: ['CHAPTER', 'I', 'THE', 'TWO', 'POETS', 'OF', 'SAFFRON',
        'PARK', 'THE', 'suburb', 'of', 'Saffron', 'Park', 'lay', 'on', 'the',
        'sunset', 'side', 'of', 'London', ',', 'as', 'red', 'and', 'ragged',
        'as', 'a', 'cloud', 'of', 'sunset', '.']

 Pretty close.
 
 * 18: Using list addition, and the set and sorted operations, compute the vocabulary of the sentences sent1 ... sent8.
 
   **Answer**: List addition is somewhat wasteful — using sets instead.

        running = set(sent1)
        running.update(sent2, sent3, sent4, sent5, sent6, sent7, sent8)
        sorted(list(running))

   We could also eliminate any items that are not composed of letters or a hyphen or ending in a period.

 * 19: What is the difference between the following two lines? Which one will give a larger value? Will this be the case for other texts?

        >>> sorted(set([w.lower() for w in text1]))
        >>> sorted([w.lower() for w in set(text1)])

   **Answer**: The results should be the same, but the first will run longer; the second reduces the number of duplicates so the `for` loop runs potentially fewer times.
   
   Wrong!
   
        In [93]: len(sorted(set([w.lower() for w in text1])))
        Out[93]: 17231
        
        In [94]: len(sorted([w.lower() for w in set(text1)]))
        Out[94]: 19317

   Because the second statement may have duplicates, distinguished by patterns of capitalization that are not eliminated in the initial `set()`; by deferring the use of `set()` until the end, the first statement eliminates the maximum number of duplicates.

 * 20: What is the difference between the following two tests: `w.isupper()` and `not w.islower()`?

   **Answer**: `not w.islower()` may return `True` for things that are not upper-case, such as numerals and punctuation; `w.isupper()` will return `True` only for upper-case.

 * 21: Write the slice expression that extracts the last two words of text2.

   **Answer**: 

        text2[-2:]

        In [1]: text2[-2:]
        Out[1]: ['THE', 'END']


 * 22: Find all the four-letter words in the Chat Corpus (text5). With the help of a frequency distribution (FreqDist), show these words in decreasing order of frequency.

   **Answer**: 

        fours = [w for w in text5 if len(w) == 4]

   This also finds some four-character non-words, like `"PM's"` and `'4:03'`, but let's assume the question means that.

        f = FreqDist(text5)
        reversed_pairs = [(v, k) for k, v in f.items()]
        list(reversed(sorted(reversed_pairs)))


[end]