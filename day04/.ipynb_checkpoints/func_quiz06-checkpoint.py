# quiz 6>
# 앞에 타자 게임을 활용
# - 1. 문제추가  2. 타자게임  3. 등수리스트  4. 종료하기
# - 문제추가 후 데이터는 파일 저장
# - 문제추가는 단어를 입력받아서 중복되지 않게 추가
# - 타자게임은 시간을 체크하고, 걸린시간을 사용자명과 함께 저장합니다. (딕셔너리로 저장: 등수데이터)
# - 등수리스트는 걸린시간이 적은 순서대로 정렬해서 출력합니다.
# - 종료하기는 등수리스트를 저장하고 진행합니다.
# - 프로그램이 시작될 때 문제와 등수정보를 읽어 옵니다.


import random,time,json
word = ['cat','dog','fox','monkey','mouse','panda','frog','snake','wolf']
# rank =
{'aaa':10000}
# with open('word.json','r'):
#     word = json.load(f)
with open('rank.json','r')as f:
    json.load(f)
while True:
    menu = input('''
------------------------------------------------------
1. 문제추가  2. 타자게임  3. 등수리스트  4. 프로그램종료  
------------------------------------------------------
메뉴 번호를 선택해주세요. ''')
    if menu == '1':
        pass
    elif menu == '2':
        input('엔터누르면 시작')
        start = time.time()

        for i in range(1,6):
            print('%s번 문제!'%(i))
            while True:
                ran = word[random.randint(0,len(word)-1)]
                answer = input('%s'%(ran))
                if not answer == ran:
                    print('틀렸습니다. 새로운 문제를 출제합니다.')
                else:
                    print('정답!')
                    break
        print('문제를 모두 풀었습니다 ㅎㅎ')
        end=time.time()
        print(f'{end-start:.0f}초')
        name = input('사용자명을 입력하세요.')
        while name in rank:
            name = input('사용자명이 중복되었습니다. 다른 이름을 입력하세요.')
        rank[name] = end-start
        print(rank)
    elif menu == '3':
        pass
    elif menu == '4':
        print('프로그램을 종료합니다.')
        with open('rank.json','w') as f:
            json.dump(rank,f)
        break
    else:
        print('메뉴선택을 잘못하셨습니다.')


import func_basic1 as fb1
import random, time, json

word = fb1.load_save_data('word.json', 'r')
rank = fb1.load_save_data('rank.json', 'r')

while True :
    menu = input('''
------------------------------------------------------
1. 문제추가  2. 타자게임  3. 등수리스트  4. 프로그램종료  
------------------------------------------------------
메뉴 번호를 선택해주세요. ''')
    if menu == '1' :
        fb1.quiz_input(word)
        with open('word.json','w', word)
    
    elif menu == '2' :
        fb1.typing_game(word,rank)

    elif menu == '3' :
        fb1.rank_list(rank)
        
    elif menu == '4' :
        print('프로그램을 종료합니다.')
        with open('rank.json', 'w') as f :
            json.dump(rank,f)
        break
    else :
        print('메뉴선택을 잘못하셨습니다.')



    elif menu == '3' :
        ranklist = sorted(rank.times(), key=lambda x:x[1])
        for index, item in enumerate(ranklist) :
            print(f'{index+1'등 {item[0]} {item[1]:.2f}')
    elif menu == '4' :
        print('프로그램을 종료합니다.')
        fb1.load_save_data




