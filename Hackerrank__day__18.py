#  Case insensitive Palindrome checking


s = input()

if s.lower() == s[::-1].lower():
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
    