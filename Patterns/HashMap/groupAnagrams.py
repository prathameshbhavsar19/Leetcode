class Solution(object):
    def groupAnagrams(self, strs):
        anadict = {}

        for s in strs:
            s_str = ''.join(sorted(s))

            if s_str in anadict:
                anadict[s_str].append(s)
            else:
                anadict[s_str] = [s]

        return list(anadict.values())


# Example usage
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    sol = Solution()
    result = sol.groupAnagrams(strs)

    print(result)