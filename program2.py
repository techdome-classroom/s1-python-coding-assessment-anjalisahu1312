def decode_message( s: str, p: str) -> bool:

# write your code here
  
  def decode_message(s: str, p: str) -> bool:
    def match(message, pattern):
        def is_match(i, j):
            if i == len(message) and j == len(pattern):
                return True
            if j == len(pattern):
                return False

            if pattern[j] == '*':
                if i < len(message) and is_match(i + 1, j):
                    return True
                return is_match(i, j + 1)

            # Handle the '?' wildcard or exact character match
            if i < len(message) and (pattern[j] == '?' or pattern[j] == message[i]):
                return is_match(i + 1, j + 1)

            # If no match is found
            return False

        return is_match(0, 0)

    # Call the match function with the input message and pattern
    return match(s, p)
  
        return False