# #6077 : [기초-종합] 짝수 합 구하기(설명)(py)
# #정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.
#
# def total(i):
#     tot = 0
#     for n in range(1, i+1):
#         if n%2==0:
#             tot+=n;
#     return tot;
#
# n = int(input())
# print(total(n))

#6078 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기(py)

def strin(ch):
    s = 'q'
    while ch != s:
        ch = input()
        print(ch)

ch = input()
print(ch)
strin(ch)