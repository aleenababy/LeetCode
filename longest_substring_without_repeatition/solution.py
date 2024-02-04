class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        result = []
        for letter in s:
            if letter not in substring:
                substring = substring + letter
                print(substring)
            else:
                result.append(substring)
                substring = letter
        # look for the longest substrings
        prev = ""
        for k in result:
            if len(k) > len(prev):
                prev = k

        return len(prev)