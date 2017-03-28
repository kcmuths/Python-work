## recursive palindrome


## Don't care about spaces and only characters matter
def toChars(s):
    import string
    s = string.lower(s) ## makes string lowercase
    ans = ''
    for c in s:  ## walk down string and gather all characters together
        if c in string.lowercase:
            ans = ans + c
    return ans

def isPal(s):
    if len(s) <= 1: ## base case. if odd or even characters.
                    ##thats why even 0 is checked
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])  ## recursive case
    
def isPalindrome(s):
    """Return True is s is a Palindrome and False otherwise"""
    return isPal(toChars(s))

print isPalindrome(' able Was I Ere i SaW eLBa')
    
