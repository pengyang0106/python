def fibo(n):
    # 请补充代码
    if n <=1:
        n = n
    else:
        n= fibo(n-1)+ fibo(n-2)
    return n


print(fibo(0))
print(fibo(6))