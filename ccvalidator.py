
def checkcard():
    sum_odds = 0
    sum_evens = 0
    temp = 0
    cardnumber = input("Please input your credit card number: ")
    cardnumber = cardnumber.replace(" ", "")
    n = len(cardnumber)
    if n != 16:
        print("Invalid Credit Card.")
        return 0;
    for x in range(15, n, -1):
        if int(cardnumber[x]) % 2 != 0:
            sum_odds += int(cardnumber[x])
        else:
            if (int(cardnumber[x]) * 2) > 9:
                temp = int(cardnumber[x]) * 2
                cardnumber[x] = str(temp[0] + temp[1])
                sum_evens += int(cardnumber[x])
                temp = 0
            else:
                sum_evens += int(cardnumber[x])
    if (sum_evens + sum_odds) % 10 == 0:
        print("Your credit card number is valid!")
    else:
        print("Your credit card number is not valid.")


checkcard()