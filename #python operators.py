#python operators

# +, -, *, /, %, //
a=10
b=5

print(a+b) #output:15
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**2)

# =,
temp_var="test"
# a=10
a=a+10
a+=10 # output: 20
a-=10 # output: 0

# ==, !=, >, <

x=1
y=2

print(x==y) # true
print(x>y) # false
print(x<y) # true
print(x>=y) # false
print(x<=y) # true

x=int(input('enter the value for var x:'))
y=int(input('enter the value for var y:'))
print(x==y)
print(x!=y)
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)

# logical ops
# and or not

print(10 == 10 and 10 > 20) #false
print(10 == 10 or 10 > 20) #false