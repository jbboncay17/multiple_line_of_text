bold="\033[1m"
end="\033[0m"

num1=float(input(bold+"Enter the first number:"+end))
num2=float(input(bold+"Enter the second number:"+end))

diff=num1-num2
print("")
print(bold+"The difference of two numbers is:"+end,diff)