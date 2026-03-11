bold="\033[1m"
end="\033[0m"

num1=int(input(bold+"Enter the first number:"+end))
num2=int(input(bold+"Enter the second number:"+end))

if num1 > num2:
    print(bold+"The smaller number is:"+end, num1)
else:
    print(bold+"The smaller number is:"+end, num2)