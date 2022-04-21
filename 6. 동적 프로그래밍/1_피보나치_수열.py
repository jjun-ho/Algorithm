
def FIB_1(n):
    f[1] = 1
    f[2] = 1
    for i in range(3,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

# 각 배열에다가 피보나치 수열 계산값 값 저장하는 변수 f 선언
f = [0]*10000

def FIB_2(n):
    if f[n] != 0:
        return f[n]
    if n==1 or n==2:
        f[n] = 1
    else:
        f[n] = FIB_2(n-1) + FIB_2(n-2)
    return f[n]

"""
* 피보나치 수열 
- 𝑓(𝑛) = 𝑓(𝑛−1) + 𝑓(𝑛−2)
- 𝑓(1) = 𝑓(2) = 1
"""