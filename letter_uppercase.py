bold="\033[1m"
end="\033[0m"

text = input(bold+"Enter text: "+end)
result = ""

for i in text:
    if i >= 'a' and i <= 'z':
        result += chr(ord(i) - 32)
    else:
        result += i
print("")
print(result)
