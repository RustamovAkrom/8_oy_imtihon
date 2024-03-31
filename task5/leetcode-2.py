class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return [int(n) for n in str(int("".join([str(i) for i in digits])) + 1)]


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([1, 2, 3]))
    print(s.plusOne([4, 3, 2, 1]))
    print(s.plusOne([9]))
