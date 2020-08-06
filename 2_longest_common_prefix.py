class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def find_prefix(word1: str, word2: str) -> str:
            res = ''
            for i in range(min(len(word1), len(word2))):
                if word1[i] == word2[i]:
                    res += word1[i]
                else:
                    break
            return res
        if strs == []:
            return ''
        solution = strs[0]
        for s in strs:
            solution = find_prefix(solution, s)
        return solution
