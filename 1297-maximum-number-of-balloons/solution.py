class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        if not text:
            return 0

        dct = {'b': 0,  'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for char in text:
            if char in dct:
                dct[char] += 1

        print(dct)

        return min(
            dct['b'] // 1, 
            dct['a'] // 1,
            dct['l'] // 2,
            dct['o'] // 2,
            dct['n'] // 1
        )


        
