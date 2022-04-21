
"""
* 최장 공통 부분 순서
- 문자열 bcdb는 문자열 (a bcb d a b)
–> 순서대로 나타나되 연속일 필요는 없음
- 문자열 bca는 문자열 (a bc bd a b)와 (b d ca ba)의 공통 부분 순서
- 문자열 bcba는 (a bcb d a b)와 (b d c a ba)의 가장 긴 공통 부분 순서 (최장 공통 부분 순서)
- C(i,j) = 0 (if. i=0 or j=0)
         = C(i-1,j-1) + 1 (if. i,j>0 and xi = yi)
         = max{ C(i-1,j) , C(i,j-1) } (if. i,j>0 and xi != yi)
"""