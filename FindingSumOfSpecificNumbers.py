Numbers_list = []

for num in range(1, 1000):
    if num % 3 == 0 or num % 5 == 0:
        Numbers_list.append(num)
print(sum(Numbers_list))