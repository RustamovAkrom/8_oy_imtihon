class Solution:
    def LenngthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


if __name__ == "__main__":
    s = Solution()
    print(s.LenngthOfLastWord("Hello World"))
    print(s.LenngthOfLastWord("   fly me   to   the moon  "))
    print(s.LenngthOfLastWord("luffy is still joyboy"))
