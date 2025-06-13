# main.py
from crawler import crawl_naver_travel, get_ai_recommended_region

def show_menu():
    print("\n" + "=" * 45)
    print("         ✈ 국내 여행지 추천 메뉴 ✈         ")
    print("=" * 45)
    print("| {:^36} |".format("1. 부산 여행지 TOP 5"))
    print("| {:^36} |".format("2. 서울 여행지 TOP 5"))
    print("| {:^33} |".format("3. 원하는 지역 여행지"))
    print("| {:^36} |".format("4. AI 추천 관광지"))
    print("| {:^37} |".format("5. 종료하기"))
    print("=" * 45)

def main():
    while True:
        show_menu()
        menu = input("원하는 메뉴 번호를 입력하세요: ").strip()

        if menu == "1":
            crawl_naver_travel("부산 가볼만한 곳")
        elif menu == "2":
            crawl_naver_travel("서울 가볼만한 곳")
        elif menu == "3":
            region = input("여행지를 검색할 지역명을 입력하세요: ").strip()
            if region:
                crawl_naver_travel(f"{region} 가볼만한 곳")
            else:
                print("⚠ 지역명을 입력하지 않았습니다.")
        elif menu == "4":
            region = get_ai_recommended_region()
            print("\n✨ AI 추천 결과 ✨")
            print(f"추천 지역: {region}")
            crawl_naver_travel(f"{region} 가볼만한 곳")
        elif menu == "5":
            print("여행지 추천 프로그램을 종료합니다. 즐거운 여행 되세요!")
            break
        else:
            print("❌ 잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.")

if __name__ == "__main__":
    main()
