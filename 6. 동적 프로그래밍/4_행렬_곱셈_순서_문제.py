
"""
* 향렬 곱셈 순서 문제
- n개의 행렬을 곱할 때 스칼라 곱하기 횟수가 가장 적은 곱하기 순서 찾기
- 행렬A: 𝑝×𝑞 행렬
- 행렬B: 𝑞×𝑟 행렬
- AB 곱 계산: 𝑝×𝑞×𝑟번의 곱하기 계산
- 행렬 곱하기 방법: (AB)C or A(BC)
- n개의 행렬 곱하기 괄호 묶는 방법:  2^n 가지
- 행렬 Ai: Pi-1 × Pi 행렬
- A1*A2* ⋯ *an 의 마지막 행렬 곱하기에 따라 n-1가지 존재
–> 𝐴1 * (A2* ⋯ *𝐴n)
–> (A1*A2)(A3* ⋯ *An)
–> (𝐴1*A2*A3) * (A4* ⋯ *An)
–> (A1* ⋯ *An-2) * (An-1* ⋯ *An)
–> (A1* ⋯ *An-1) * An
- C(i,j):  Ai ... Aj를 계산하는 최소 비용
-> Ai * (Ai+1 ... Aj) , (Ai*Ai+1) * (Ai+2 ... Aj), ... , (Ai ... Aj-1) * Aj 중 하나
-> (Ai*Ak) * (Ak+1 ... Aj)의 최소비용: C(i,j) + C(k+1,j) + (Pi-1 * Pk * Pj)
- C(i,j) = 0 (if. i=j)
         = min{ C(i,j) + C(k+1,j) + (Pi-1 * Pk * Pj) } (if. i<j, i <= k <= j-1)
"""
