class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Sanity check: lengths must add up
        if len(s1) + len(s2) != len(s3):
            return False
        
        cache = {}

        def dfs(i, j):
            # Base Case: If we have successfully used up both strings
            if i == len(s1) and j == len(s2):
                return True
            
            # Check if we have already solved this state
            if (i, j) in cache:
                return cache[(i, j)]
        
            # Try to consume a character from s1
            # Note: s3 index is always i + j
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            
            # Try to consume a character from s2
            # CRITICAL FIX: s2[j], not s2[i]
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
            
            # If neither path works, this state is a failure
            cache[(i, j)] = False
            return False
            
        return dfs(0, 0)