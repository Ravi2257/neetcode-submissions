class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ''.join(ch for ch in s.lower() if ch.isalnum())
        print(news)
        if news[::-1] == news:
            return True
        else:
            return False
