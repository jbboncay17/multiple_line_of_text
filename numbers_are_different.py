bold="\033[1m"
end="\033[0m"
green="\033[32m"
red="\033[31m"

num1=int(input(bold+"Enter the first number:"+end))
num2=int(input(bold+"Enter the second number:"+end))

if num1 == num2:
    print(bold+green+"The numbers are equal"+end)
else:
    print(bold+red+"The numbers are not equal"+end)