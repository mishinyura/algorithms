def main(lst, search):
    # amount = int(input())
    # lst = list(map(int, input().split()))
    # search = int(input())

    if search in lst:
        print(search)
    else:
        temp = lst[0]
        for i in lst[1:]:

            if abs(i - search) < abs(temp - search):
                temp = i
        print(temp)





if __name__ == '__main__':

    main([1, 2, 3, 4, 7, 8], 6)
    main([1, 2, 3, 4, 5, 7], 6)
    main([1, 2, 3, 4, 8], 6)
    main([1, 2, 3, 8], 6)

# 6
# 1 2 3 4 7 8
# 6