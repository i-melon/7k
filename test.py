n =int(input('введите двузначное число: '))
m = int(input('введите трехзначное число: '))
firstDigit = m//100
lastDigit = m%10
print(n+firstDigit+lastDigit)