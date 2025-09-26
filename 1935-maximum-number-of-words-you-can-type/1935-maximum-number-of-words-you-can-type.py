class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l = len(text) - 1
        bk = set(brokenLetters)
        words = text.split(" ")
        ans = 0

        for i in words:
            for c in i:
                if c in bk:
                    ans += 1
                    break

        return len(words) - ans

        