"""The goal of this interview is to implement trie (or prefix tree) using dictionaries, where:

the dictionary keys are the prefixes
the value of a leaf node is None in Python and nil in Ruby.
Examples:

>>> build_trie("trie")
{'t': {'tr': {'tri': {'trie': None}}}}
>>> build_trie("tree")
{'t': {'tr': {'tre': {'tree': None}}}}
>>> build_tree("A","to", "tea", "ted", "ten", "i", "in", "inn")
{'A': None, 't': {'to': None, 'te': {'tea': None, 'ted': None, 'ten': None}}, 'i': {'in': {'inn': None}}}
>>> build_trie("true", "trust")
{'t': {'tr': {'tru': {'true': None, 'trus': {'trust': None}}}}}


"""


def build_trie(word):
    trie = {}
    trie.setdefault(word)

    trie = recursive_trie(trie, word[:-1])
    print('returned: ', trie)
    return trie


def recursive_trie(trie_dict, word):
    print(trie_dict, word)
    if word == '':
        return trie_dict, print('returning: ', trie_dict)
    trie_dict = ({word: trie_dict})
    recursive_trie(trie_dict, word[:-1])


t = build_trie("trie")
print(t)
