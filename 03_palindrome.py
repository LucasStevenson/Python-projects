print("Type in a word or phrase and see whether it is a palindrome or not")
s = input().replace(" ", "")

if len(s) < 1:
    print("Well of course a 1 digit word/letter is a palindrome!")

if s.lower() == s[::-1].lower():
    print("true")
else:
    print("false")
