def checkpalindrome(string,i):
    if i >= len(string) // 2:
        return True
    if string[i] != string[len(string) - i -1]:
        return False
    return checkpalindrome(string,i+1)
 

## Two pointer method
def checkPalindrome(str):
    left ,right = 0,len(str) - 1
    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True
            
if __name__ == "__main__":
    print(checkpalindrome("racecar",0))
    print(checkPalindrome("racecar"))