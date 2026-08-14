class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        pseudocode
        - lp = 0, rp = len(s) - 1
        while lp < rp:
        - check if lp and rp are alphanumric
        - if both == alphanumeric
            if s[lp] == s[rp]
                lp +=1
                rp -= 1
            else:
                return False
        - elif lp == alphanumeric
            lp += 1
        - elif rp == alphanumeric
            rp -= 1
        
        else:
            lp += 1
            rp -= 1
        return True

        '''

        lp, rp = 0, len(s) - 1
        while lp < rp:
            if s[lp].isalnum() and s[rp].isalnum():
                if s[lp].lower() == s[rp].lower():
                    lp += 1
                    rp -= 1
                else:
                    print(s[lp])
                    return False
            elif s[lp].isalnum():
                rp -= 1
            elif s[rp].isalnum():
                lp += 1
            else:
                lp += 1
                rp -= 1
        return True