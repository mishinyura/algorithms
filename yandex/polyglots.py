def main():
    amount_students = int(input())
    known_by_all = None
    known_by_any = set()

    for _ in range(amount_students):
        amount_words = int(input())
        langs = set(input() for _ in range(amount_words))

        if known_by_all is None:
            known_by_all = langs.copy()
        else:
            known_by_all &= langs

        known_by_any |= langs

    print(len(known_by_all))
    for lang in sorted(known_by_all):
        print(lang)

    print(len(known_by_any))
    for lang in sorted(known_by_any):
        print(lang)


if __name__ == '__main__':
    main()