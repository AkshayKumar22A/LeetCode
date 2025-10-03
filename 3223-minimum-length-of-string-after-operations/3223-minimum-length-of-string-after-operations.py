class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        rem = 0
        for x in count.values():
            while x >= 3:
                rem += 2
                x -= 2
        return len(s) - rem
        