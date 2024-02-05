

def is_palindrome(string):
    rev = ''.join(reversed(string))
    if rev == string:
	print ('given string is a palindrome')
    else:
	print('given string is not a palindrome'