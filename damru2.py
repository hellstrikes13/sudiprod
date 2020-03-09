n = input('enter no for printing damru: ')
for i in list(range(1,n+1))[:-1]: print i * '*' + (n-i) * ' ' + (n-i) * ' ' + i * '*'
print '*' * (n*2)
for i in list(range(n,0,-1))[1:]: print i * '*' + (n-i) * ' ' + (n-i) * ' ' + i * '*'
