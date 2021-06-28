def calcsum(x):
    y = 0
    for num in range(x + 1):
        y += num
        return y
    
num = int(input("정수를 입력하세요: "))
result = calcsum(num)
print("1 ~ %d까지의 누적합: %d" % (num,result))