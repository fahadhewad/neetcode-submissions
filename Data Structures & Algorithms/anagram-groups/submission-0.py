class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            character_counts = {}
            for char in word:
                character_counts[char] = character_counts.get(char, 0) + 1

            
            key = tuple(sorted(character_counts.items()))

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        
        return list(groups.values())