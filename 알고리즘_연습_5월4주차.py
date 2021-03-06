# -*- coding: utf-8 -*-
"""알고리즘 연습-5월4주차.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12o4XC4G2czTr1Ry2UBWnN7hA3FZNAxIk

## 1010번 다리 놓기-S5
"""

num = int(input())

cnt = 0
while cnt < num:
    cnt += 1
    a, b = map(int, input().split())

    c = 1
    d = 1
    for i in range(1, a+1):
        c *= b
        b -= 1

        d *= a
        a -= 1
    print(int(c/d))

"""while문 쓰는 것 보다 이렇게 for문 쓰는게 더 편함"""

for _ in range(int(input())): 
  a, b = map(int, input().split())
  c = 1
  d = 1
  for i in range(1, a+1):
    c *= b
    b -= 1

    d *= a
    a -= 1
  print(int(c/d))

"""함수 만들어서 사용 factorial, comb"""

def facto(x):
  if x == 0 or x == 1:
    return 1
  else:
    return x * facto(x-1)

def comb(n, r):
  return int(facto(n) / (facto(r)*facto(n-r)))

for _ in range(int(input())):
  a, b = map(int, input().split())
  print(comb(b, a))

"""숏코드 : math의 comb 활용"""

import math

for _ in range(int(input())):
    n,m = map(int,input().split())
    print(math.comb(m,n))

"""## 1018번 체스판 다시 칠하기-S5

첫번째 문자를 기준으로 계산
"""

n,m=map(int,input().split())

chess_board =[]
for i in range(n):
    chess_board.append(input())

move_array=[]
for i in range(n-7):
    for j in range(m-7):
        move=0
        new_chess_board=[]
        board_size_n=8
        board_size_m=8
        for k in range(board_size_n):
            
            new_chess_board.append(chess_board[k+i][j:j+8])#8개의 규격으로 자른 chess_board 생성
        
        for k in range(board_size_n): #생성된 체스판에서 하나씩 훑기
            for l in range(board_size_m):
                if new_chess_board[0][0]=='B': 
                    if (l+k) % 2 ==0:# 맨 앞에것이 B일 때, l+k가 짝수인 것은 문자가 같아야 한다.
                        if new_chess_board[k][l]=='W':
                            move +=1
                    else:
                        if new_chess_board[k][l]=='B':# 맨 앞에것이 B일 때, l+k가 홀수인 것은 문자가 달라야 한다.
                            move +=1
                if new_chess_board[0][0]=='W':
                    if (l+k) % 2 ==0:# 맨 앞에것이 W일 때, l+k가 짝수인 것은 문자가 같아야 한다.
                        if new_chess_board[k][l]=='B':
                            move +=1
                    else:
                        if new_chess_board[k][l]=='W':# 맨 앞에것이 B일 때, l+k가 홀수인 것은 문자가 달라야 한다.
                            move +=1
        if move > 32:
            move = 64-move

        move_array.append(move)


print(min(move_array))

# 체스판 받아오기
M, N = map(int, input().split(' '))
board = [input() for _ in range(M)]

min_fill = 64

# 8*8로 구성된 체스판 옮겨가면서 체크
for m in range(M-7):
    for n in range(N-7):
        chess = [b[n:n+8] for b in board[m:m+8]]
        
        chess_inline = ''.join(chess[::2]) + ''.join(chess[1::2])[::-1]  # 새로운 inline을 만든다 : 바꿔야할 개수를 세기 위해서 -> 결과값 확인해보기
       
        start_B = chess_inline[::2].count('B') + chess_inline[1::2].count('W')
        
        start_W = 64 - start_B
        
        min_fill = min(min_fill, start_B, start_W)

print(min_fill)

# VS code로 각 위치의 결과 확인하면서 이해하기

"""## 2839번 설탕배달 - B1

상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
"""

N = int(input())

n1 = (N // 5) + ((N % 5) // 3) # 5로 나누고 나머지를 3으로 나눔
n2 = (N // 3) # 3으로 나눈 몫, 3의 배수로만 나눌 수 있는경우(예 : 6, 12)

n = (N % 5) % 3 # 5로 나눈 나머지를 3으로 나눈 나머지
m = (N % 3)

if n != 0 and m != 0:
  print(-1)
elif n == 0:
  print(n1)
else:
  print(n2)

# 11 을 처리하지 못함 5 1개와 3의 배수의 조합 or 5 2개와 3의배수의 조합 등

"""조합을 만들고 최소값을 반환하는 형태로 해결 -> 런타임에러-> -1 조건을 안넣어줬었음"""

N = int(input())

y = []

for i in range(1001):  
    for j in range(1000):
        
        m = 5*i + 3*j
        if N == m:
            x = i+j
            y.append(x)

if y:
  print(min(y))
else:
  print(-1)

"""숏코드 : 수학적으로 이해가 되어야 짤 수 있을 듯"""

a=int(input())
print(-(a in[4,7]) or a//5+(a%5!=0)+(a%5 in[2,4]))

n=int(input())
cnt,mod = divmod(n,5) #divmod ?
print(-1 if cnt<mod%3 else cnt+mod//3+mod%3)

n=int(input())
r=n%5
while r%3!=0:
    r+=5
if(n-r<0):
    print(-1)
else:
    print(r//3+(n-r)//5)

inp=int(input())
r=(0,1,0)
if(inp in (4,7)):print(-1)
else:print(int(inp/5)+int(inp%5/3)+inp%5%3)

"""# 1065번 한수 찾기 -S4

어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
"""

#99까지는 모두 한수, 공차가 양수, 0, 음수 모두 가능

N = int(input())

cnt = 0
for i in range(1, N+1):
  if i < 100:
    cnt += 1
  else:
    strN = str(i)

    if int(strN[0])+int(strN[2]) == int(strN[1])*2:
      cnt+= 1

print(cnt)

"""숏코드"""

count=0
for i in range(1,int(input())+1):  # 숫자 받아서 그만큼 for문 돌리기
  if(i<100):                       # 1부터 99까지는 모두 한수로 처리
    count+=1
  else:
    a,b,c,*_=map(int, str(i))      # i를 str로 받고 그것을 각각 int로 바꾼 후 a,b,c,*_로 분리
    count+=(a-b==b-c)              # 한수 조건 만족하면 True(1)이 되므로 이를 하나씩 더함
print(count)

a, b, c, _ = map(int, str(1524))
print(a)
print(type(a))
print(b)
print(c)
print(_)

"""# 1152번 단어의 개수 -S3

영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 공백 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 또한 문자열은 공백으로 시작하거나 끝날 수 있다.

첫째 줄에 단어의 개수를 출력한다.
"""

def count_word(sent):
  sent = sent.split()
  cnt = len(sent)

  return cnt

sent = input()

print(count_word(sent))

count_word('The last character is a blank ')

"""숏코드"""

print(len(input().split()))

"""#15829 Hashing - S2

APC에 온 것을 환영한다. 만약 여러분이 학교에서 자료구조를 수강했다면 해시 함수에 대해 배웠을 것이다. 해시 함수란 임의의 길이의 입력을 받아서 고정된 길이의 출력을 내보내는 함수로 정의한다. 해시 함수는 무궁무진한 응용 분야를 갖는데, 대표적으로 자료의 저장과 탐색에 쓰인다.

이 문제에서는 여러분이 앞으로 유용하게 쓸 수 있는 해시 함수를 하나 가르쳐주고자 한다. 먼저, 편의상 입력으로 들어오는 문자열에는 영문 소문자(a, b, ..., z)로만 구성되어있다고 가정하자. 영어에는 총 26개의 알파벳이 존재하므로 a에는 1, b에는 2, c에는 3, ..., z에는 26으로 고유한 번호를 부여할 수 있다. 결과적으로 우리는 하나의 문자열을 수열로 변환할 수 있다. 예를 들어서 문자열 "abba"은 수열 1, 2, 2, 1로 나타낼 수 있다.

해시 값을 계산하기 위해서 우리는 문자열 혹은 수열을 하나의 정수로 치환하려고 한다. 간단하게는 수열의 값을 모두 더할 수도 있다. 해시 함수의 정의에서 유한한 범위의 출력을 가져야 한다고 했으니까 적당히 큰 수 M으로 나눠주자. 짜잔! 해시 함수가 완성되었다. 이를 수식으로 표현하면 아래와 같다.

 
\[H = \sum_{i=0}^{l-1}{a_i} \mod M\] 

해시 함수의 입력으로 들어올 수 있는 문자열의 종류는 무한하지만 출력 범위는 정해져있다. 다들 비둘기 집의 원리에 대해서는 한 번쯤 들어봤을 것이다. 그 원리에 의하면 서로 다른 문자열이더라도 동일한 해시 값을 가질 수 있다. 이를 해시 충돌이라고 하는데, 좋은 해시 함수는 최대한 충돌이 적게 일어나야 한다. 위에서 정의한 해시 함수는 알파벳의 순서만 바꿔도 충돌이 일어나기 때문에 나쁜 해시 함수이다. 그러니까 조금 더 개선해보자.

어떻게 하면 순서가 달라졌을때 출력값도 달라지게 할 수 있을까? 머리를 굴리면 수열의 각 항마다 고유한 계수를 부여하면 된다는 아이디어를 생각해볼 수 있다. 가장 대표적인 방법은 항의 번호에 해당하는 만큼 특정한 숫자를 거듭제곱해서 곱해준 다음 더하는 것이 있다. 이를 수식으로 표현하면 아래와 같다.

 
\[H = \sum_{i=0}^{l-1}{a_ir^i} \mod M\] 

보통 r과 M은 서로소인 숫자로 정하는 것이 일반적이다. 우리가 직접 정하라고 하면 힘들테니까 r의 값은 26보다 큰 소수인 31로 하고 M의 값은 1234567891(놀랍게도 소수이다!!)로 하자.

이제 여러분이 할 일은 위 식을 통해 주어진 문자열의 해시 값을 계산하는 것이다. 그리고 이 함수는 간단해 보여도 자주 쓰이니까 기억해뒀다가 잘 써먹도록 하자.

첫 줄에는 문자열의 길이 L이 들어온다. 둘째 줄에는 영문 소문자로만 이루어진 문자열이 들어온다.

입력으로 주어지는 문자열은 모두 알파벳 소문자로만 구성되어 있다.

문제에서 주어진 해시함수와 입력으로 주어진 문자열을 사용해 계산한 해시 값을 정수로 출력한다.

예제 1: abcde의 해시 값은 1 × 31^0 + 2 × 31^1 + 3 × 31^2 + 4 × 31^3 + 5 × 31^4 = 1 + 62 + 2883 + 119164 + 4617605 = 4739715이다.

예제 2: zzz의 해시 값은 26 × 31^0 + 26 × 31^1 + 26 × 31^2 = 26 + 806 + 24986 = 25818이다.
"""

import string

alp = list(string.ascii_lowercase)

alp.index('a')+1

import string

alp = list(string.ascii_lowercase)

n = int(input())
sent = input()
m = 1234567891
result = 0

for i in range(n):
    c = alp.index(sent[i])+1
    result += c*31**i

print(result%m)

"""숏코드"""

input()   # 개수는 받을 필요 없고
a=input()
s=0
for i in range(len(a)):
    t=ord(a[i])-96   # ord가 무엇? a=97로 되어 있음, 따라서 -96
    s+=t*31**i
print(s%1234567891)   # M으로 나눈 나머지를 출력(주어진 해싱 함수)

ord('a'), ord('b')

"""#2562 최댓값 1+

9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

"""

number = []

for i in range(9):
  number.append(int(input()))

m = max(number)

print(m)
print(number.index(m)+1)

"""숏코드"""

x = [int(input()) for _ in range(9)]
print(max(x), x.index(max(x))+1)

"""2675 문자열 반복 1+

문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다.

각 테스트 케이스에 대해 P를 출력한다.
"""

n = int(input())

for _ in range(n):
    num,s = input().split()
    for j in range(len(s)):
        print(s[j]*int(num), end='')
    print()

"""숏코드
- join과 내포문 사용
"""

for i in range(int(input())):
    b,c=input().split()
    print(''.join(j*int(b) for j in c))

"""# 10951 A+B(readlines이용)

"""

import sys
lines = sys.stdin.readlines()

for line in lines:
    a, b = map(int, line.split())
    print(a+b)