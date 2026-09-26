class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each string, create dict/arr of chars
        # key: dict/arr -> value: string
        # return list version

        groups = defaultdict(list)
        
        for word in strs:
            curr = [0] * 26

            # create mapping for each word
            for char in word:
                curr[ord(char) - ord('a')] += 1
            groups[tuple(curr)].append(word)
        
        return list(groups.values())

        # HASH TABLE | time: O(mn), space: O(mn)
        # for each string, create character frequency array, convert to tuple
        # as key and append original string to correspond w frequency tuple
        # hash map: {frequency tuple : matching strings}
        stringMap = defaultdict(list)
        for s in strs:
            frequency = [0] * 26
            for char in s:
                frequency[ord(char) - ord('a')] += 1
            stringMap[tuple(frequency)].append(s)
        return list(stringMap.values())

        # SORTING + HASH MAP | time: O(mnlogn), space: O(mn)
        # for each string, append original string to correspond w sorted string
        # hash map: {sorted string : matching strings}
        stringMap = defaultdict(list)
        for s in strs:
            stringMap[tuple(sorted(s))].append(s)
        return list(stringMap.values())

            
        