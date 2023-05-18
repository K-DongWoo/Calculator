#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

class Calculator:   
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def squared(self, x, y):
        return x ** y

    def modulo(self, x, y):
        return x % y

    def square_root(self, x):  #제곱근
        return math.sqrt(x)

    def variance(self, nums):  #분산
        n = len(nums)
        mean = sum(nums) / n
        return sum((x-mean) ** 2 for x in nums) / n

    def std_deviation(self, nums):   #표준편차
        return math.sqrt(self.variance(nums))

    def time_change(self,x):   #초→(시간:분:초)
        return f'{x//3600}:{x%3600//60}:{x%60}'

    def exp(self,x):    #지수 e^x를 반환합니다
        return math.exp(x)

    def sin(self,x):     #사인값
        return math.sin(x)

    def cos(self,x):     #코사인값
        return math.cos(x)

    def tan(self,x):     #탄젠트
        return math.tan(x)

    def asin(self,x):     #역사인값
        return math.asin(x)

    def acos(self,x):     #역코사인값
        return math.acos(x)

    def atan(self,x):     #역탄젠트값
        return math.atan(x)
    
    def factorial(self,x):
        if x == 1:      # n이 1일 때
            return 1    # 1을 반환하고 재귀호출을 끝냄
        return x * cal.factorial(x - 1)
    
    def fabs(self, x):    #절대값
        return math.fabs(x)
    
    
    def deter(self, n):   # 행렬식
        l = []
        
        print('한 행씩 입력!!(예: 1 2)')

        for i in range(n):
            a = list(map(int, input().split()))
            l.append(a)

        if n == 2:
            return (l[0][0]*l[1][1]) - (l[0][1]*l[1][0])

        #else:
            # 3차 행렬식
           
     def calculate_regression_line(self, x_values, y_values):
    n = len(x_values)
    if n != len(y_values):
        raise ValueError("x값의 수와 y값의 수는 같아야 합니다.")
    
    # x, y, x^2, xy의 합을 계산합니다.
    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_x_squared = sum(x ** 2 for x in x_values)
    sum_xy = sum(x * y for x, y in zip(x_values, y_values))

    # 기울기 (m)와 y절편 (b)을 계산합니다.
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    y_intercept = (sum_y - slope * sum_x) / n
    #coefficients = np.polyfit(x_values, y_values, 1)
    #p = np.poly1d(coefficients)
    return slope, y_intercept



cal = Calculator()
print("계산 가능한 연산 목록")
print("더하기(+)   빼기(−)   곱하기(×)   나누기(÷)   제곱(**)  나머지(%)  제곱근(√)  분산 표준편차 시간계산(h:m:s)  지수(e)")  
print("사인(sin)  코사인(cos)  탄젠트(tan)  역사인(asin)  코사인(acos)  탄젠트(atan)  행렬식(det)")



while True:
    choice = input("수식 선택>>")
    if choice == '더하기' or choice == '+':
        while True: 
            try:
                num1 = float(input("첫번째 숫자>>"))
                num2 = float(input("두번째 숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
                continue
        print(num1, "+", num2, "=", cal.add(num1, num2))

    elif choice == '빼기' or choice == '-':
        while True:
            try:
                num1 = float(input("첫번째 숫자>>"))
                num2 = float(input("두번째 숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
                continue
        print(num1, "-", num2, "=", cal.subtract(num1,num2))

    elif choice == '곱하기' or choice == '*':
        while True: 
            try:
                num1 = float(input("첫번째 숫자>>"))
                num2 = float(input("두번째 숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
                continue
        print(num1, "*", num2, "=", cal.multiply(num1,num2))

    elif choice == '나누기' or choice == '/':
        while True: 
            try:
                num1 = float(input("첫번째 숫자>>"))
                num2 = float(input("두번째 숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
                continue
        print(num1, "/", num2, "=", cal.divide(num1,num2))

    elif choice == '제곱' or choice == '**':
        while True: 
            try:
                num1 = float(input("첫번째 숫자>>"))
                num2 = float(input("제곱할 수>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
                continue
        print(num1, "**", num2, "=", cal.squared(num1,num2))

    elif choice == '나머지' or choice == '%':
        while True: 
            try:
                num1 = float(input("첫번째 숫자>>"))
                num2 = float(input("나눌 수>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
                continue
        print(num1, "%", num2, "=", cal.modulo(num1,num2))

    elif choice == '제곱근' or choice == '√':
        while True: 
            try:
                num = float(input("숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
        print("√", num, "=", cal.square_root(num))

    elif choice == '분산':
        nums = []
        while True:
            try:
                input_data = input("데이터를 입력하세요(구분자: 공백 또는 쉼표)>> ")
                nums = [float(x) for x in input_data.replace(",", " ").split()]
                if len(nums) < 2:
                    print("데이터를 두 개 이상 입력하세요")
                    continue
                else:
                    break
            except ValueError:
                print("숫자를 입력하세요")
                continue
        print("분산:", cal.variance(nums))

    elif choice == '표준편차':
        nums = []
        while True:
            try:
                input_data = input("데이터를 입력하세요(구분자: 공백 또는 쉼표)>> ")
                nums = [float(x) for x in input_data.replace(",", " ").split()]
                if len(nums) < 2:
                    print("데이터를 두 개 이상 입력하세요")
                    continue
                else:
                    break
            except ValueError:
                print("숫자를 입력하세요")
                continue
        print("표준편차:", cal.std_deviation(nums))

    elif choice == '시간계산' or choice == 'h:m:s':
        while True: 
            try:
                num = int(input("숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
                continue
        print(num,"초", "=", cal.time_change(num),"(시간:분:초)")

    elif choice == '지수' or choice == 'e':
        while True: 
            try:
                num = float(input("숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
        print("e^", num, "=", cal.exp(num))

    elif choice == '사인' or choice == 'sin':
        while True: 
            try:
                num = float(input("숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
        print("sin", num, "=", cal.sin(num))

    elif choice == '코사인' or choice == 'cos':
        while True: 
            try:
                num = float(input("숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
        print("cos", num, "=", cal.cos(num))

    elif choice == '탄젠트' or choice == 'tan':
        while True: 
            try:
                num = float(input("숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
        print("tan", num, "=", cal.tan(num))

    elif choice == '역사인' or choice == 'asin':
        while True: 
            try:
                num = float(input("숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
        print("asin", num, "=", cal.asin(num))

    elif choice == '약코사인' or choice == 'acos':
        while True: 
            try:
                num = float(input("숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
        print("acos", num, "=", cal.acos(num))

    elif choice == '역탄젠트' or choice == 'atan':
        while True: 
            try:
                num = float(input("숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
        print("atan", num, "=", cal.atan(num))

    elif choice == '팩토리얼' or choice == '!':
        print("숫자를 입력하세요")
        num1 = float(input(" "))
        print(num1, "!", "=", cal.factorial(num1))
        
    elif choice == '절대값' or choice == 'fabs':
        while True: 
            try:
                num = float(input("숫자>>"))
                break
            except ValueError:
                print("숫자를 입력하세요")
        print('fabs', num, "=", cal.fabs(num))
        
        
    elif choice == '행렬식' or choice == 'det':
        while True:
            try:
                n = int(input('행렬의 차원 입력 : '))
                break
            
            except ValueError:
                print("숫자를 입력하세요")
                continue
        
        print(cal.deter(n))
    
    elif choice == '회귀직선':
        while True:
        try:
            input_data = input("y값을 입력하세요(구분자: 공백 또는 쉼표)>> ")
            y_values = [float(y) for y in input_data.replace(",", " ").split()]
            if len(y_values) != len(x_values):
                print("x값의 수와 y값의 수가 같아야 합니다")
                continue
            else:
                break
        except ValueError:
            print("숫자를 입력하세요")
            continue
    slope, y_intercept = cal.calculate_regression_line(x_values, y_values)
    print("기울기:",slope)
    print("y 절편:",y_intercept )
    print("회귀직선: y의 예측값 =",y_intercept ,"+", slope, "x")
    regression_line = np.poly1d([slope, y_intercept])

    plt.scatter(x_values, y_values)  # 데이터 산점도 그래프
    plt.plot(x_values, regression_line(x_values), "r")  # 회귀직선 그래프
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Regression Line")
    plt.show()
        
        
    elif choice == '종료':
        print("사용종료")
        break
    else:
        print("잘못된 입력입니다.")
        continue

