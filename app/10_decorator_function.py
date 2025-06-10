# 쉽게 설명: https://wikidocs.net/184210

import time
from typing import Callable, Any


# 클로저 함수
def modules():
    def f1(x):
        print("f1 called with", x)
        return pow(x, 2)
    return f1

# nested 함수 call
f1 = modules()
print(f1(4))

# 클로저 함수 - 인자처리
def mul(m):
    def wrapper(n):
        return m * n
    return wrapper

f2 = mul(m=3)
print(f2(4))


# 데코레이터 사용하지 않고 로그 출력에 활용 예시
def elapsed(original_func):   # 기존 함수를 인수로 받는다.
    def wrapper():
        start = time.time()
        result = original_func()    # 기존 함수를 수행한다.
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))  # 기존 함수의 수행시간을 출력한다.
        return result  # 기존 함수의 수행 결과를 리턴한다.
    return wrapper

def myfunc():
    for i in range(1000):
        for j in range(1000):
            if i==j and (i+1) > 999:
                print(i)

elapsed(myfunc)()  # myfunc 함수를 elapsed 함수로 감싸서 실행한다.

# print(1/0)

# 데코레이터 사용해서 로그 출력에 활용 예시
def elapsed(original_func):   # 기존 함수를 인수로 받는다.
    def wrapper():
        start = time.time()
        result = original_func()    # 기존 함수를 수행한다.
        end = time.time()
        print("함수 수행시간: %f 초" % (end - start))  # 기존 함수의 수행시간을 출력한다.
        return result  # 기존 함수의 수행 결과를 리턴한다.
    return wrapper

@elapsed
def myfunc():
    for i in range(10000):
        for j in range(10000):
            if i==j and (i+1) > 9990:
                print(i)

myfunc()


# 로그 출력에 활용 예시: 함수가 인자를 받는 경우 
def elapsed(original_func):   # 기존 함수를 인수로 받는다.
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)    # 기존 함수를 수행한다.
        end = time.time()
        print(original_func.__name__, "함수 수행시간: %f 초" % (end - start))  # 기존 함수의 수행시간을 출력한다.
        return result  # 기존 함수의 수행 결과를 리턴한다.
    return wrapper

@elapsed
def myfunc(msg):
    for i in range(10000):
        for j in range(10000):
            if i==j and (i+1) > 9990:
                print(msg, i)

# 인자를 넘겼기 때문에 에러가 발생한다.
# myfunc("You need python")

# *args, **kwargs 문을 사용해 인자가 그래도 넘어갈 수 있도록 수정한다.
myfunc("You need python")




# # 교재 고급 예제  소스 ###########################################
# Recieve arguments for decorator function
def custom_fence(fence: str = "+"):
    # Decorator function
    def add_fence(func):
        # Original function wrapper
        def wrapper(text: str):
            print(fence * len(text))
            func(text)
            print(fence * len(text))
        
        return wrapper
    
    return add_fence



# Use custom decorator
@custom_fence("-")
def log(text: str):
    print(text)

# Call function with defined name
log("ballon")



def custom_fence(title: str = "Log", repit_text: str = "+", repit_count: int = 10, print_text: str = "Hello World"):
    # Decorator function
    def add_fence(func):

        def wrapper(*args, **kwargs):
            print(print_text)
            print(title, repit_text * repit_count)
            func(*args, **kwargs)
            print(title, repit_text * repit_count)
        
        return wrapper
    return add_fence


# Use custom decorator
@custom_fence("테스트", "-", 20, "안녕하세요")
def log(text: str):
    print(text)

log("감사합니다다")


# # Function Typing
def decorator( func: Callable[[Any], None] ):
#              argument/s type ☝️    👆 return type
    pass



