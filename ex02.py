print('Sequência de Fibonacci')
print('--'*30)
print('--'*30)
print('--'*30)

t1 = 0
t2 = 1
t3 = 3
i = int(input('Digite um número que você acha que pertence a Sequência de Fibonacci: '))
print('--'*30)
print('--'*30)


while i > t3:
    t3 = t1 + t2
    t1 = t2
    t2 = t3

if i == 0:
    print('O número 0 está na Sequência de Fibonacci.')

elif i == t3:
    print('O número está na Sequência de Fibonacci.')

else:
    print('Esse número não faz parte da Sequência de Fibonacci.')

print('--'*30)