class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        first = strs[0]
        prefix = ""

        for i in range(len(first)):
            for word in strs:
                if i>= len(word) or word[i] != first[i]:
                    return prefix
                    exit()
            prefix += first[i]
        return prefix