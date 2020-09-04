n=int(input())
def reduceB(a, b) : 
      
    # Initialize result 
    mod = 0
  
    # Calculating mod of b with a  
    # to make b like 0 <= b < a 
    for i in range(0, len(b)) : 
          
        mod = (mod * 10 + ord(b[i])) % a 
  
    return mod      # return modulo 
    
def sieve(n):
    prime=[True]*(n+1)
    for i in range(2,n+1):
        if(prime[i]):
            for j in range(i*i,n+1,i):
                prime[j]=False
    s=set()
    for i in range(2,n+1):
        if(prime[i]):
            s.add(i)
    return len(s)
print(sieve(n))