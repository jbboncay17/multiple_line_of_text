bold='\033[1m'
end='\033[0m'
green='\033[32m'

num1 = int(input(bold+"Enter first number: "))
num2 = int(input(bold+"Enter second number: "))
print("")
sum = num1 + num2
print(bold+green+"The sum of the two numbers is:"+end, sum)