'''
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
'''


def anagrams(word, words):
    word_dic = {k:sorted(list(word)).count(k) for k in sorted(list(word))}
    words_dic = [{k:sorted(list(word)).count(k) for k in sorted(list(word))} for word in words]
    indeces = [i for i, dic in enumerate(words_dic) if dic == word_dic]
    return [words[i] for i in indeces] if indeces else []




print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(['aabb', 'bbaa'])
assert anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa']
assert anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer']
assert anagrams('laser', ['lazing', 'lazy', 'lacer']), []