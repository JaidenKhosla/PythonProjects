def collatz(n: int):
    if n == 0: return 0
    steps = 0
    while n != 1:
        print(n)
        steps+=1
        if n%2==0:
            n//=2
        else:
            n = n//2+1
    return steps

