from random import randint


def lotto_numbers_roll():
    lotto_numbers = []
    while len(lotto_numbers) < 6:
        number = randint(1, 49)
        if number not in lotto_numbers:
            lotto_numbers.append(number)
    lotto_numbers = sorted(lotto_numbers)
    print(lotto_numbers)
    return lotto_numbers


def get_number():
    while True:
        num = (input("Enter a number: "))
        try:
            num = int(num)
            break
        except ValueError:
            print("Please enter a number")

    return num


def get_numbers():
    user_numbers = []
    while len(user_numbers) < 6:
        num = get_number()
        if num not in user_numbers and num >= 1 and num <= 49:
            user_numbers.append(num)
        else:
            print("Please enter a number between 1 and 49 that is not already in list")
    user_numbers = sorted(user_numbers)
    print(user_numbers)
    return user_numbers


def lotto_result():
    user_numbers = get_numbers()
    lotto_numbers = lotto_numbers_roll()
    score = 0

    for number in lotto_numbers:
        if number in user_numbers:
            print(number)
            score += 1
    print(score)


lotto_result()




