#주민등록번호 14자리를 입력받아서 성별을 체크합니다.
#프로그램 종료는 (q,Q)를 누를때 까지 반복처리합니다.

#입력예제 : 123456-1234567
#조건처리 : 길이값 체크 / 성별 체크(가능값1,2,3,4)
#출력 : 여서입니다. or 남성입니다.




## 입력 : 주민등록번호
## 리턴값 : 성별

def jumin_check1(jumin) :
    gender = ''
    if len(jumin) == 14 and jumin[6] == '-' and jumin[7] in ['1','2','3','4'] :
        if jumin[7] in ['1','3'] :
            gender = '남성'
        else :
            gender = '여성'
    else :
        print('입력 문자의 길이가 안맞거나, 성별값의 범위가 아닙니다.')
    return gender

while True :
    invalue = input('주민등록번호 입력(14자리, 종료:q,Q) >>> ')
    if len(invalue) == 1 and invalue.lower() == 'q' :
        print('프로그램 종료')
        break


    gender = jumin_check1(invalue)
    print(gender)