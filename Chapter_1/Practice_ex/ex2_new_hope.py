
frase1 = 'A long time ago in a galaxy '
frase2 = 'far away...'
n = int(input())
middle = 'far, '

if n == 1:
    print(frase1 + frase2)
else:
    print(frase1 + ((n-1) * middle) + frase2)



