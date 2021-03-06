import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
import time

# ID PW 수강신청 정보 설정
ID = input('ID를 입력하세요 ')
PW = input('PW를 입력하세요 ')
print('(학수번호,분반,검색시 몇번째 위치)를 입력하세요 ex)106245 001 1    [그만 입력 하려면 대문자 X를 입력하세요]')
informations = []
while True:
    input_line = input()
    if input_line == 'X':
        break
    information = []
    information.append(input_line.split(' ')[0])
    information.append(input_line.split(' ')[1])
    information.append(input_line.split(' ')[2])
    informations.append(information)

# ChromeOptions 설정
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# options 넣은 driver 변수 생성 후 driver 설정
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(time_to_wait=10)
driver.maximize_window()

# 학사정보 시스템 URL 접속
driver.get('https://portal.sejong.ac.kr/jsp/login/loginSSL.jsp?rtUrl=sjpt.sejong.ac.kr/main/view/Login/doSsoLogin.do?p=')

# 키보드 보안 팝업 취소 후 확인
Alert(driver).dismiss()
Alert(driver).accept()

# ID PW 입력후 로그인 버튼 클릭
driver.find_element_by_xpath(
    "/html/body/form/div[2]/div/div[2]/div[1]/input").send_keys(ID)
driver.find_element_by_xpath(
    "/html/body/form/div[2]/div/div[2]/div[2]/input").send_keys(PW)
driver.find_element_by_xpath("/html/body/form/div[2]/div/div[2]/a").click()
time.sleep(1)

# 해상도 검사 하기
if driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[1]/div/div[1]/div").text == "※ 화면해상도는 1280x1024에 최적화 되어 있습니다. 최적화 해상도보다 작은 창을 이용하실경우 스크롤이 생성되어 이용에 불편하실 수 있습니다.":
    driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[1]/div/div[2]/a").click()

# Simple_GUI 인지 검사 하기
Simple_GUI = False
if driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/ul/li/div[1]/a').text == "수강신청":
    Simple_GUI = True

if Simple_GUI:
    # NEXT 버튼 클릭
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/a').click()
    time.sleep(1)

else:
    # 수업/성적 클릭
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]/span").click()

    # 강좌조회 및 수강신청 클릭
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/table/tbody/tr[1]/td[3]/span").click()

    # 수강신청 클릭
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/table/tbody/tr[2]/td[2]/div/div[4]/table/tbody/tr/td[3]/span").click()

    # NEXT 버튼 클릭
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div[2]/a").click()
    time.sleep(1)

index = 0
while True:
    index = index % len(informations)

    if Simple_GUI:
        # 학수번호 입력
        driver.find_element_by_xpath(
        "/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]/table[2]/tbody/tr[2]/td[3]/div[3]/input[1]").clear()
        driver.find_element_by_xpath(
        "/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]/table[2]/tbody/tr[2]/td[3]/div[3]/input[1]").send_keys(informations[index][0])

        # 분반 입력
        driver.find_element_by_xpath(
        "/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]/table[2]/tbody/tr[2]/td[3]/div[3]/input[2]").clear()
        driver.find_element_by_xpath(
        "/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]/table[2]/tbody/tr[2]/td[3]/div[3]/input[2]").send_keys(informations[index][1])
    
    else:
        # 학수번호 입력
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/table[2]/tbody/tr[2]/td[3]/div[3]/input[1]").clear()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/table[2]/tbody/tr[2]/td[3]/div[3]/input[1]").send_keys(informations[index][0])
    
        # 분반 입력
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/table[2]/tbody/tr[2]/td[3]/div[3]/input[2]").clear()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/table[2]/tbody/tr[2]/td[3]/div[3]/input[2]").send_keys(informations[index][1])

    # 검색 버튼 클릭
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]/table[2]/tbody/tr[2]/td[5]/a").click()
    time.sleep(1)

    # 신청 버튼 클릭
    if informations[index][2] == '1':
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div/table/tbody/tr[1]/td[2]/button").click()
    elif informations[index][2] == '2':
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div/table/tbody/tr[2]/td[2]/button").click()
    elif informations[index][2] == '3':
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div/table/tbody/tr[3]/td[2]/button").click()
    elif informations[index][2] == '4':
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div/table/tbody/tr[4]/td[2]/button").click()
    elif informations[index][2] == '5':
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div/table/tbody/tr[5]/td[2]/button").click()
    elif informations[index][2] == '6':
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div/table/tbody/tr[6]/td[2]/button").click()
    elif informations[index][2] == '7':
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div/table/tbody/tr[7]/td[2]/button").click()
    elif informations[index][2] == '8':
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div/table/tbody/tr[8]/td[2]/button").click()
    elif informations[index][2] == '9':
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div/table/tbody/tr[9]/td[2]/button").click()
    else:
        print('검색 시 위치 오류 입니다. 검색 시 위치를 정확하게 입력 해주세요.')
        exit()
    time.sleep(1)

    # "선택한 과목을 수강신청 하시겠습니까?" 확인 클릭
    driver.find_element_by_xpath(
        "/html/body/div[6]/div[2]/div[1]/div/div[2]/a[2]").click()
    time.sleep(1)

    # "수강여석이 없습니다" 확인 클릭 or "신청 되었습니다 재조회 하시겠습니까?" 취소 클릭
    driver.find_element_by_xpath(
        "/html/body/div[6]/div[2]/div[1]/div/div[2]/a").click()
    time.sleep(1)

    index = index+1