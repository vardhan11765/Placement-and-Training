def count_primes(n):
    c=[]
    for i in range(2,n):
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
                break
        if flag==0:
            c.append(i)
    return c
print(count_primes(10))