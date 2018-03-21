y=raw_input('Enter the number: ')
y=int(y)
low=0
high=y
x=(high+low)/2
guess=0
while(abs(x**2-y)>.01):
     guess+=1
     if(x**2>y):
         high=x
     else:
         low=x
     x=(high+low)/2
print('No. of guesses= '+str(guess)+', '+'answer= '+str(x))     
