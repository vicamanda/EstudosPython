def fibonacci_for(termos):
    a, b = 0, 1
    print("Sequência de Fibonacci (for):")
    for _ in range(termos):
        print(a, end=' ')
        a, b = b, a + b

fibonacci_for(10)