def reverse_word(word: str) -> str:
    index = len(word) - 1
    rev_word = ''
    while True:
        rev_word += word[index]
        index -= 1
        if index < 0:
            break
    return rev_word

def get_words(text: str) -> list:
    lst = []
    temp = ''
    for let in text:
        if let == ' ' and temp:
            lst.append(reverse_word(temp))
            temp = ''
        else:
            temp += let
    if temp:
        lst.append(reverse_word(temp))
    return lst

def main():
    text = 'first_word second_word!! second_word!!'
    for i in get_words(text):
        print(i)

if __name__ == '__main__':
    main()