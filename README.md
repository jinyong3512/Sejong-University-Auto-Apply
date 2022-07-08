<p align='center' style='font-size:150%'>Sejong-University-Auto-Apply는 자동화 크롬을 통해 수강신청을 계속 합니다.</p>

# :star: 특징
## Main.java
>1. [검사 필요] 수강신청 기간 작동
>2. [검사 필요] 수강신청 변경 기간 작동
### Main.java 과정
>1. ID PW informations 입력 받음
>2. URL 접속 후 보안 팝업 취소 확인
>3. ID PW 입력 후
## Main.py
>1. [검사 필요] 수강신청 기간 작동



# :white_check_mark: 실행방법

## 1.  Git Bash를 이용하여 clone
```    
$ cd .. 
$ cd .. 
$ (/c 에서) git clone https://github.com/jinyong3512/Sejong-University-Auto-Apply.git
```    
>("Updating files: 100% (7645/7645), done." 라고 나오면 그때부터 사용 가능)

## 2.  chromedriver 다운 받기

>본인 컴퓨터의 크롬 버전을 확인한 후 크롬 버전에 맞는 chromedriver.exe를 다운로드합니다.

>크롬 버전 확인 방법: https://blog.naver.com/kiddwannabe/221539689821

>chromedriver.exe 다운: https://chromedriver.chromium.org/downloads

>C드라이브에 있는 Sejong-University-Auto-Apply 안에 chromedriver.exe를 자신이 다운받은 chromedriver.exe로 덮어주세요.

## 3.  보안 프로그램 삭제 하기

>학교 로그인할 때 쓰는 키보드 보안 프로그램을 삭제해야 합니다.

>프로그램 추가/제거에서 nProtect Online Security V1.0을 제거해 주세요!



## 4.  실행 도구

### Java  
>IDE로 프로젝트를 열고 **Run Main.java**
>(꼭 프로젝트로 Sejong-University-Auto-Apply 열어야함 !)
>(IDE Intellij 추천!)

### Python  
>1. cmd 열고 'pip install selenium'
>2. [IDE로 프로젝트를 열고 **Run Main.py**] 혹은 [**Main.py** 오른쪽 마우스 눌러서 **Edit with idle**로 열어서 **Run**]
>
>(IDE로 열려면 꼭 프로젝트로 Sejong-University-Auto-Apply 열어야함 !)


# 😞 한계
> 1. 여러 과목을 입력 해놔도 하나라도 성공할 시 프로그램이 멈춥니다.
> 
> 2. 학수 번호+분반 검색 시 여러 수업이 뜰 경우  
> 예를 들어 순번 3번이 성공할 경우 순번 4번에 있던 게 3번이 되기 때문에  
> 수강신청에 성공했지만 안 멈추고 계속 신청할 수 있습니다.
>
> 3. 보안 문자 뚫을 확률이 30% 정도 되는 것 같습니다.


# :page_with_curl: 라이센스
>APACHE LICENSE, VERSION 2.0
