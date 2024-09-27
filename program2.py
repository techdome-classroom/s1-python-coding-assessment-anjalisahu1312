def decode_message( s: str, p: str) -> bool:

# write your code here
  
  def is_match(message, pattern):
    # Get the lengths of the message and pattern
    m, n = len(message), len(pattern)
    
    # Create a DP table with dimensions (m+1) x (n+1), initialized to False
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # An empty pattern matches an empty message
    dp[0][0] = True
    
    # Handle patterns that start with one or more '*' symbols
    for j in range(1, n + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[j - 1] == message[i - 1] or pattern[j - 1] == '?':
                # Current characters match or '?' matches any single character
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                # '*' matches zero or more characters
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    
    return dp[m][n]

# Test cases
print(is_match("aa", "a"))    # Output: False
print(is_match("aa", "*"))    # Output: True
print(is_match("cb", "?a"))   # Output: False
        return False