class String:
    def __init__(self, text: str) -> None:
        self.text = text

    def get_amount_words(self) -> int:
        sings = ['.', '!', '?', ',', ' ']
        temp = ''
        if self.text:
            count = 1
        else:
            return 0
        for let in self.text:
            if let in sings and temp:
                if temp not in sings:
                    count += 1
                temp = ''
            else:
                temp += let


        return count

    def get_amount_sentences(self) -> int:
        sings = ['.', '!', '?']
        if self.text:
            count = 1
            temp = ''
        else:
            return 0
        for let in self.text:
            if let in sings and temp:
                if temp not in sings:
                    count += 1
                temp = ''
            else:
                temp += let
        return count



def main():
    string = String('First.Second word! And You!?!!! Hello')
    print(string.get_amount_words())
    print(string.get_amount_sentences())

if __name__ == '__main__':
    main()