num = int(input())
first = (num // 1000) ** 2
second = (num % 1000 // 100) ** 2
third = (num % 100 // 10) ** 2
fourth =(num % 10) ** 2
result = int(str(first) + str(second) + str(third) + str(fourth))
print(result)