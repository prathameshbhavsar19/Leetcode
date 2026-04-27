class Solution(object):
    def isPalindrome(self, s):
        cs = ''.join(char.lower() for char in s if char.isalnum())
        return cs == cs[::-1]


if __name__ == "__main__":
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    print(sol.isPalindrome(s))  # True