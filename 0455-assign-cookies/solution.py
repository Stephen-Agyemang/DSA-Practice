class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        if not s or not g:
            return 0 

        # satisfiable_children = 0
        # max_s = max(s)
        # m = len(s)

        # for factor in g:
        #     if factor <= max_s and m > 0:
        #         satisfiable_children += 1
        #         m -= 1
        #         print(satisfiable_children)

        # if satisfiable_children <= len(s):
        #     return satisfiable_children

        # else:
        #     return satisfiable_children - len(s)

        g.sort()
        s.sort()

        kid_pointer = 0
        cookie_pointer = 0

        while kid_pointer < len(g) and cookie_pointer < len(s):
            if s[cookie_pointer] >= g[kid_pointer]:
                kid_pointer += 1

            cookie_pointer += 1

        return kid_pointer
