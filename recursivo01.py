def fibonacci(termo):
    if termo <= 1:
        return termo
    return fibonacci(termo - 1) + fibonacci(termo - 2)

termo = int(input("Informe um termo para a sequência de Fibonacci >>"))
print(fibonacci(termo))
