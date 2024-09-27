def decodef decode_message(s: str, p: str) -> bool:
    # This function will call the match function to check if the message matches the pattern
    def match(message, pattern):
        def is_match(i, j):
            # If we reach the end of both the message and pattern, it's a match
            if i == len(message) and j == len(pattern):
                return True
            # If only the pattern is exhausted but not the message, it's not a match
            if j == len(pattern):
                return False

            if pattern[j] == '*':

                if i < len(message) and is_match(i + 1, j):
                    return True
                return is_match(i, j + 1)
            
            if i < len(message) and (pattern[j] == '?' or pattern[j] == message[i]):
                return is_match(i + 1, j + 1)

            return False

        return is_match(0, 0)

    return match(s, p)