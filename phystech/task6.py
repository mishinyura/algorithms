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
            temp = reverse_word(temp)
            lst.append(temp)
            temp = ''
        else:
            temp += let
    if temp:
        lst.append(temp)
    return lst

def main():
    text = 'first_word second_word!!  d'
    for i in get_words(text):
        print(i)

if __name__ == '__main__':
    main()