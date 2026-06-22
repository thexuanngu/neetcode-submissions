class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Solves the Interleaving String problem using 2D Tabulation (Bottom-Up DP).
        
        Time Complexity: O(M * N) - We visit every cell in the grid once.
        Space Complexity: O(M * N) - We store a full 2D boolean grid.
        """
        
        # 1. Sanity Check
        # If the total characters don't match, s3 cannot be formed by s1 + s2.
        if len(s1) + len(s2) != len(s3):
            return False

        # 2. Initialize DP Table
        # Create a grid of size (len(s1) + 1) x (len(s2) + 1).
        # We need the +1 to represent the "empty string" state at the end.
        # dp[i][j] answers: "Can s3[i+j:] be formed by s1[i:] and s2[j:]?"
        dp = [ [False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        # 3. Base Case (Bottom-Right Corner)
        # If s1 is empty and s2 is empty, they form an empty s3. This is True.
        dp[len(s1)][len(s2)] = True

        # 4. Iterate Backwards
        # We start from the end of the strings and move to the beginning (0,0).
        # We do this because to solve index (i, j), we need the results 
        # from (i+1, j) and (i, j+1).
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                
                # Check Option A: Take character from s1
                # 1. Ensure i is within bounds (i < len(s1))
                # 2. Does s1's current char match s3's current target?
                # 3. If we take from s1, is the remainder valid (dp[i+1][j])?
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                
                # Check Option B: Take character from s2
                # 1. Ensure j is within bounds (j < len(s2))
                # 2. Does s2's current char match s3's current target?
                # 3. If we take from s2, is the remainder valid (dp[i][j+1])?
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
                    
        # 5. Return Result
        # The answer for the entire strings starting at index 0
        return dp[0][0]