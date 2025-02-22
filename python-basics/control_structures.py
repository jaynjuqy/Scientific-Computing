def is_even_or_odd(num: int) -> None:
    if num%2 > 0 :
        print(f'The number {num} is odd')
        return
    else:
        print(f'The number {num} is even')
        return

if __name__ == "__main__":
    user_num = int(input("Enter a number for even or odd classification: "))
    is_even_or_odd(user_num)

    x: int = 10
    while x != 0:
        print(f'X: {x}')
        x -=1

    even_nums: list = []
    for num in range(1, 50):
        if num % 2 == 0:
            even_nums.append(num)

    print(f'Even numbers between 1 and 50 are: {even_nums}')
