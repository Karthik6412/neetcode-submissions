class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = s.lower()
        i = 0
        j =len(s) - 1
        while (i<j):
            print(s[i], "is i right now before check ")
            print(s[j], "is j right now  before check ")
            if s[i].isalnum() != True:
                print(s[i], "is alphanumeric so skipping")
                i += 1
                continue
            if s[j].isalnum() != True:
                print(s[j], "is alphanumeric so skipping")
                j -= 1
                continue
            if s[i] == s[j]:
                print(s[i], "is i right now when they are equal ")
                print(s[j], "is j right now  when they are equal ")
                i += 1
                j -= 1
            else:
                print(s[i], "is i and ", s[j], "is j and it's not equal")
                return False
        return True