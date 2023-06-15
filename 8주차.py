want = int(input())
# # want = int(str(input()))
# # want = int(str(15))
# # want = int("15")
# # want = 15


정수값 두개를 입력받아주시구요
그값을 a,b 에 초기화 시켜주세요
그 a,b를 사칙연산(6개)한 결과를
(병렬) 나란히 출력해주세요( 한 줄 출력해줘 )
그 때 구분해주는 녀석은요 "-"로 부탁드릴게요
a = int(input())
b = int(input())

ans1 = a + b
ans2 = a - b
ans3 = a * b
ans4 = a / b
ans5 = a // b
ans6 = a % b
print(ans1,ans2,ans3,ans4,ans5,ans6,sep = "-")
선생님 — 2023.04.06. 오후 9:04
입력받아 계산 4
정수 입력받아 계산
실수 받아 그대로 출력
길이 단위 환산하기
실수 입력받아 계산 2
정수를  2 개 나란히 입력받아서
두개를 더한값, 그리고 두개를 뺀값을 나란히 출력해주세요
그때 출력되는 두 값은 : 요거로 구분해주세요
a=3 # a|3| int
b=6 # b|6| int
a,b = map(int,input().split(" "))
5 7
a = int(input()) # a = 5
b = int(input()) # b = 7
5
7
print(a,b)
