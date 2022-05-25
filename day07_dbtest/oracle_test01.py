import cx_Oracle

conn = cx_Oracle.connect('scott', 'tiger', 'localhost:1521/xe')
cursor = conn.cursor()
cursor.execute("select * from emp")

while True :
    choice = input('1. 직무별 사원  2. 사원명 검색  3. 프로그램 종료 >>> ')

    if choice == '1' :
        while True :
            work = input('직무를 입력해주세요.(종료:q 또는 Q) >>> ')

            if work.lower() == 'q' :
                print('메뉴로 돌아갑니다.')
                break
            
            no = 0
            for item in cursor :
                if work == item[2] :
                    no = 1
                    print(item)
            if no == 0 :
                print('존재하지 않는 직무입니다.')


    if choice == '2' :
        while True :
            name = input('사원명을 입력해주세요.(종료:q 또는 Q) >>> ')

            if name.lower() == 'q' :
                print('메뉴로 돌아갑니다.')
                break
            else :
                cursor.execute("SELECT * FROM emp WHERE ename like '%" + name + "%'")

    if choice == '3' :
        print('프로그램을 종료합니다.')
        break

conn.close()
Hi
Hello