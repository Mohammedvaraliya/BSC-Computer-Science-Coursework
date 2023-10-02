P = 23
G = 9

print('The Value of P is :%d'%(P))
print('The Value of G is :%d'%(G))
print("\n")

a = 4
print('Secret Number for Alice is :%d'%(a))

b = 6
print('Secret Number for Bob is :%d'%(b))
print("\n")

x = int(pow(G,a,P))
print("Key generated from Alice is :%d"%x)
y = int(pow(G,b,P))
print("Key generated from Bob is :%d"%y)
print("\n")

ka = int(pow(y,a,P))
kb = int(pow(x,b,P))

print('Secret key for the Alice is : %d'%(ka))
print('Secret Key for the Bob is : %d'%(kb))