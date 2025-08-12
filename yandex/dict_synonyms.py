import sys


def main():
    amount = int(input())
    synonyms = {}
    reverse_synonyms = {}
    for _ in range(amount):
        f_word, s_word = input().split()
        synonyms[f_word] = s_word
        reverse_synonyms[s_word] = f_word
    word = input()

    if word in synonyms:
        print(synonyms[word])
    else:
        print(reverse_synonyms[word])


if __name__ == '__main__':
    main()