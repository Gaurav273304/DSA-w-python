def checkpalindrome(string,i):
    if i >= len(string) // 2:
        return True
    if string[i] != string[len(string) - i -1]:
        return False
    return checkpalindrome(string,i+1)
    
if __name__ == "__main__":
    print(checkpalindrome("racecar",0))