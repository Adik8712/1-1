#     DEF

# def lessons():
#     return 2 + 2


# print(lessons())

# def summ(x: int, y=123):
#     return x + y

# a = int(input('Введите первое число: '))
# # b = int(input("Введите второе число: "))

# print(summ(a, 2))


# def name(a, b=2):


# def name(a, b=2, c=None) -> None:
#     return 

# print(name(10, 10, 10))

# def name(a, b=2, c=None):
#     """
#     Наша функция вернет тебе Привет мир
#     """
    
#     return "Привет мир"


# name(1, 2, 3)

def cal(x,y,z):
    import os

    with open('user_cal.txt', "a") as file:
        if z=="+":
            os.system('clear')
            file.write(f"Пользователь сделал запрос: {x} {z} {y} = {x+y}\n")
            return f"{x} {z} {y} = {x+y}"
    
        elif z=='-':
            os.system('clear')
            file.write(f"Пользователь сделал запрос: {x} {z} {y} = {x-y}\n")
            return f"{x} {z} {y} = {x-y}"
    
        elif z=='*':
            os.system('clear')
            file.write(f"Пользователь сделал запрос: {x} {z} {y} = {x*y}\n")
            return f"{x} {z} {y} = {x*y}"
        
        elif z=='/':
            if y!=0:
                os.system('clear')
                file.write(f"Пользователь сделал запрос: {x} {z} {y} = {x/y}\n")
                return f"{x} {z} {y} = {x/y}"
            
            else:
                os.system('clear')
                file.write(f"Пользователь сделал плохой запрос: {x} {z} {y} = ???\n")
                return 'На ноль делить нельзя!'
            
        elif z=='%':
            if y!=0:
                os.system('clear')
                file.write(f"Пользователь сделал запрос: {x} {z} {y} = {x%y}\n")
                return f"{x} {z} {y} = {x%y}"
            
            else:
                os.system('clear')
                file.write(f"Пользователь сделал плохой запрос: {x} {z} {y} = ???\n")
                return 'На ноль делить нельзя!'
            
        elif z=='**':
            os.system('clear')
            file.write(f"Пользователь сделал запрос: {x} {z} {y} = {x**y}\n")
            return f"{x} {z} {y} = {x**y}"
        
        elif z=='//':
            if y!=0:
                os.system('clear')
                file.write(f"Пользователь сделал запрос: {x} {z} {y} = {x//y}\n")
                return f"{x} {z} {y} = {x//y}"
            
            else:
                os.system('clear')
                file.write(f"Пользователь сделал плохой запрос: {x} {z} {y} = ???\n")
                return 'На ноль делить нельзя!'
            
        else:
            os.system('clear')
            file.write(f"Пользователь сделал плохой запрос: {x} {z} {y} = ???")
            return "Данной операции нема!"
        

while True:
    num = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    oper = input("Введите операцию: ")
    print(cal(num, num2, oper))

























