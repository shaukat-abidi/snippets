
'''
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest  substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
class Solution:
    def lengthOfLongestSubstring_greedy(self, s: str) -> int:
        longest_substring = []
        dict_string = {}
        len_longestSubstring = 1
        len_string = len(s)

        # Edge case
        if len_string < 2:
            return len_string
        
        for start in range(len_string-1):
            start_chr = s[start]
            dict_string = {}
            longest_substring = []
            # Init vars
            longest_substring.append(start_chr)
            dict_string[start_chr] = True
            len_currentString = 1
            for end in range(start+1, len_string):
                end_chr = s[end]
                print(start,end)
                if end_chr in dict_string:                    
                    # print(f'end_chr found in dictionary:{end_chr} -> {dict_string}, longest_substring:{longest_substring}')
                    break
                else:
                    longest_substring.append(end_chr)
                    dict_string[end_chr] = True
                    len_currentString += 1
                    len_longestSubstring = max(len_longestSubstring, len_currentString)
                print(f"longest_substring: {longest_substring}")

        return len_longestSubstring
                
        

        

if __name__ == '__main__':
    sol = Solution()
    s="dvdbfe" #vdf is the largest one
    print(sol.lengthOfLongestSubstring_greedy(s))
    print('all good')