palindrome = input('Enter the value:')
reverse = palindrome[:: -1]
if(palindrome == reverse):
    print('True')
else:
    print('False')