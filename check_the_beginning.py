bold="\033[1m"
end="\033[0m"
red="\033[31m"
green="\033[32m"
black="\033[30m"

text=input(bold+black+"Enter your text:"+end)
word=input(bold+black+"Enter the starting word/letter to check:"+end)
print("")
if text[:len(word)]==word:
    print(bold+green+"Correct"+end)
else:
    print(bold+red+"Incorrect"+end)
