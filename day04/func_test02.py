def add(*args) :  #튜플로 저장하는 함수
    print(args)

add(1,2,3,4,5,6,7,8,9)


def addd(*args) :
    total = 0
    for i in args :    # i는 지역변수
        total += i
    return total

total = addd(1,2,3,4,5,6,7,8,9)
print(total)


def mul(a,b,c,d) :
    print(a*b*c*d)

mul(*[1,2,3,4])