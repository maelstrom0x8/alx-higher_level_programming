#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 0 or n >= len(s):
        return s  # Return the original string if index is out of range
    result = ''
    for i in range(len(s)):
        if i != n:
            result += s[i]
    return result
