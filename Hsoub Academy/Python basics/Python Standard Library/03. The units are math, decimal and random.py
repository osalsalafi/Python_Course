# ------------------------------------------------
# -- 03. The units are math, decimal and random --
# ------------------------------------------------
import math

# Greatest common divisor
print(math.gcd(4,6,14,20)) #2

print("#---------------------------------#")
#Least common multiple
print(math.lcm(4,6,14,20)) #420

print("#---------------------------------#")
# floor, ceil
print(math.floor(4.6)) #lower = 4
print(math.ceil(4.1)) #higher = 5
print(round(4.6)) # = 5
print(round(4.4)) # = 4

print("#---------------------------------#")
# exponential
print(math.exp(0)) #1.0

# b^x = n == x = logb n 

print("#---------------------------------#")
# power
print(math.pow(2,4)) # b = 2, x = 4 >> n = 16

print("#---------------------------------#")
# log
print(math.log(16,2)) # n = 16, b = 2 >> x = 4
print(math.log10(1000)) #3.0
print(math.log(1000,10)) #2.9999999999999996

print("#---------------------------------#")
# square root
print(math.sqrt(16)) #4

print("#---------------------------------#")
# pi, e
print(math.pi) # 3.141592653589793
print(math.e) # 2.718281828459045

print("#-------------------------------------------------------------#")
import decimal

# float not equal to decimal
print(0.1+0.1+0.1 == 0.3) #False

# getcontext
# print(decimal.getcontext()) #Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
decimal1 = decimal.Decimal(3)
decimal2 = decimal.Decimal("3.14")
decimal3 = decimal.Decimal(2/4)
float1 = 3
float2 = 3.14

print(decimal1) #3
print(decimal2) #3.14
print(decimal3) #0.5

print(float1 + float2) #6.140000000000001
print(decimal1+decimal2) #6.14

print("#---------------------------------#")
# min, max, sum
decimals = [decimal1, decimal2, decimal3]
print(min(decimals)) #0.5
print(max(decimals)) #3.14
print(sum(decimals)) #6.64

# some of the math function are available 
print(decimal1.sqrt()) #1.732050807568877293527446342

# for more info https://wiki.hsoub.com/Python/decimal

print("#-------------------------------------------------------------#")
import random

print(random.randint(1,100)) #27
print(random.randrange(100)) #75
num = [1,6,4,9,7]
print(random.choice(num)) #7
print(random.choices(num)) #[7]
print(random.choices(num, k=3)) #[6, 7, 4]
random.shuffle(num)
print(num) # [6, 7, 4, 1, 9]

# for more info "Generate pseudo-random numbers"
