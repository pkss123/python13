foods = {}

while True:
    print("\n======음식점 메뉴 관리 프로그램======")
    print("1. 신규 메뉴 등록")
    print("2. 메뉴판 전체 보기")
    print("3. 프로그램 종료")
    num = int(input("> "))
    
    if num == 1:
        name = input("메뉴명 : ")
        
        if name in foods:
            print("이미 등록된 메뉴입니다")
        else:
            price = input("가격 : ")
            foods[name] = price
            print("신규 메뉴 %s(이)가 등록 되었습니다" % name)
    elif num == 2:
        print("-"*40)
        print("1. 기존 메뉴 수정| 2. 메뉴 삭제| 3. 나가기")
        select = int(input(">"))
        if select == 1:
            name = input("가격을 변경할 메뉴의 이름을 입력하세요 : ")
        
            if name in foods:
                newprice = input("변경할 가격 입력 : ")
                foods[name] = newprice
                print("%s의 가격이 %s원으로 변경되었습니다" % (name))
            else:
                print("%s(은)는 등록된 메뉴가 아닙니다" % name)
        elif select == 2:
            name = input("삭제할 메뉴의 이름을 입력하세요 : ")
            if name in foods:
                del foods[name]
                print("%s이(가) 삭제되었습니다" % name)
            else:
                print("%s(은)는 등록된 메뉴가 아닙니다" % name)
                
        
        if select == 3:
            break
    
        print("\n------메뉴판------")
        menulist = foods.keys()
        for menu in menulist:
            print(menu,":",foods[menu],"원")
    if num == 3:
        break