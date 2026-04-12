from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map each frequency signature to the list of matching anagrams.
        groups = defaultdict(list)

        for word in strs:
            # Count how many times each letter appears in the current word.
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1

            # Convert the count list to a tuple so it can be used as a hashable key.
            groups[tuple(count)].append(word)

        # Return only the grouped anagrams.
        return list(groups.values())

        