class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        balloon = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        if len(text) < len(balloon):
            return 0

        for char in text:
            if char in balloon:
                balloon[char] += 1

        
        return min(
            balloon['b'] // 1,
            balloon['a'] // 1,
            balloon['l'] // 2,
            balloon['o'] // 2,
            balloon['n'] // 1,
        )
