def sequencia_fibonacci(n):
    sequencia_fib = [0, 1]
    while sequencia_fib[-1] < n:
        sequencia_fib.append(sequencia_fib[-1] + sequencia_fib[-2])
    return sequencia_fib

def verificacao(num):
    sequencia_fib = sequencia_fibonacci (num)
    
    
    if num in sequencia_fib:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."


print(verificacao(21))  
print(verificacao(22))  
