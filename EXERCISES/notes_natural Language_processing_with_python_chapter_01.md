## Exercises, Natural Language Processing with Python, Chapter 1


 * 4: How many words are there in text2?

        In [1]: len(text2)
        Out[1]: 141576

   How many distinct words are there?

        In [2]: len(set(text2))
        Out[2]: 6833

 * 6: Produce a dispersion plot of the four main protagonists in Sense and Sensibility: Elinor, Marianne, Edward, and Willoughby. What can you observe about the different roles played by the males and females in this novel? Can you identify the couples?

        text2.dispersion_plot(['Elinor', 'Marianne', 'Edward', 'Willoughby'])

   The female characters appear much more than the male.

   Couples are hard to make out. But Edward and Willoughby seem to appear in alternation!

 * 7: Find the collocations in text5.

        text5.collocations()

 * 15: Find all words in the Chat Corpus (text5) starting with the letter b. Show them in alphabetical order.

        sorted(set([i for i in text5 if i.startswith('b')]))

or

        sorted(set([i for i in text5 if i and i[0] == 'b']))

 * 17: Use text9.index() to find the index of the word sunset. You’ll need to insert this word as an argument between the parentheses. By a process of trial and error, find the slice for the complete sentence that contains this word.



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
 
   List addition is somewhat wasteful — using sets instead.

        running = set(sent1)
        running.update(sent2, sent3, sent4, sent5, sent6, sent7, sent8)
        sorted(list(running))

   We could also eliminate any items that are not composed of letters or a hyphen.