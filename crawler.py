import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# AI 추천 지역 목록 (장소 제외)
ai_regions = [
    "서울", "부산", "제주도", "속초", "경주", "전주", "춘천", "여수"
]

# AI 지역만 추천
def get_ai_recommended_region():
    return random.choice(ai_regions)

# 네이버 지도 검색 및 출력 함수
def crawl_naver_travel(query):
    print(f"\n[ '{query}' 네이버 지도 검색 결과 ]")
    print("-" * 50)

    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--log-level=3')
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    url = f"https://map.naver.com/p/search/{query.strip()}"
    driver.get(url)
    time.sleep(5)

    try:
        driver.switch_to.frame("searchIframe")
        time.sleep(2)

        cards = driver.find_elements(By.CSS_SELECTOR, "div.YgcU0")

        if not cards:
            print("⚠ 장소 정보를 찾지 못했습니다.")
            return

        for i, card in enumerate(cards[:5], 1):
            try:
                name = card.find_element(By.CSS_SELECTOR, "span.xBZDS").text.strip()
                category = card.find_element(By.CSS_SELECTOR, "span.LF32u").text.strip()
                print(f"{i}. {name} - {category}")
            except:
                print(f"{i}. (정보를 불러올 수 없습니다)")

    except:
        print("⚠ 오류 발생: 검색 결과를 불러오지 못했습니다.")
    finally:
        print("\n✅ 모든 정보를 출력했습니다. 크롬 창을 닫습니다.")
        try:
            driver.quit()
        except:
            pass
