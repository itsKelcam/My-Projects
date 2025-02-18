
def even_odd_check(num):
    for num in range(1,51):
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is odd")
even_odd_check(1)

def even_odd_check_2(num1):
    while num1 <= 50:
        if num1 % 2 == 0:
            print(f"{num1} is even")
        else:
            print(f"{num1} is odd")
        num1 += 1

even_odd_check_2(1)