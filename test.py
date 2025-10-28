""" print ("hello skibidi sigmas")
def number(x):
    if x % 2==0:
        print(f"{x} is even")
    elif x % 2==1:
        print(f"{x} is odd")
    else:
        print (f"{x} is decimal")
number (2.2) """
""" print ("heres the check")
bills=800
float (bills)
service = input("how was the service")

def get_tip(service, bills):
    if service == 'good':
        x = bills * .2
        print(x)
    elif service == 'okay':
        x = bills * .15
        print(x)
    elif service == "bad":
        x = bills *.0
        print (x)
    elif service == "great":
        x = bills * 0.25
        print(x)

get_tip(service, 800) """

""" def all_factors(number):
    factors=[]
    for i in range(1, number+1):
        if number % i == 0 :
            factors.append(i)
    return factors
print(all_factors(67))
print(all_factors(92))

def find_gcd(x,y):
    gcf = 0
    for i in range(1, x+1):
        if x % i ==0 and y % i == 0:
            gcf = i
    return gcf
print (find_gcd(100,1000))

print ("heres, your clues, 1006+11 but in a dumb way or just 100623-12")
answer=input ("find za code")
if answer==("100611"):
    print (" u get a cookie eventually one day idk when tho")
elif answer==("1017"):
    print ("i said in a dumb way not the normal way")
else:
    print ("bad boyyyyyyyyyyyyyyyyyyyy")
    
sentence = input()
e_count= sentence.count ('e')+ sentence.count ('E')
if e_count > 5:
    print ("e heavy")
else:
    print ("e light") """



import random 
numbers= [1,2,3,4,5,6,7,8,9,10]
number = random.choice (numbers)
guesses = []

for i in range(number):
    
       
    guess = int(input("Guess boi"))
    guesses.append(guess)
    if guess == number:
        print("correct",guesses)
        break
    elif guess > number:
        print ("smaller than your guess")
    elif guess < number:
        print ("greater than your guess")

print (guesses)
