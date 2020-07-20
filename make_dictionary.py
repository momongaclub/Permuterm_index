import sys


def make_index(words):
    indexies = []
    for word in words:
        word = word + '$'
        word_len = len(word)
        word_indexies = []
        for i in range(word_len):
            f = word[0]
            word = word[1:]
            word = word + f
            word_indexies.append(word)
        indexies.append(word_indexies)
    return indexies


def main():
    words = ['fhalfha;', 'fkalh', 'a']
    indexies = make_index(words)
    print(indexies)


if __name__ == '__main__':
    main()
