M, N = list(map(int, input().split()))
if M*N % 2 == 0:
    print(int(M*N/2))
else:
    print(int((M*N-1)/2))