# given a string, find the length of the longest substring without repeating characters
# lists - append to a list. not repeating - convert to a string - len(string)

class Solution:
    def lengthoflongestsubstring(self, s):
        ls = ''
        str_list = []
        for i in s:
            if i in ls:
                str_list.append(ls)
                ls = ''
                continue
            ls += i
        print(str_list)
        print(max(str_list, key=len))
        return len(max(str_list, key=len))

print (Solution().lengthoflongestsubstring('abrkaabcdefghijjxxx'))