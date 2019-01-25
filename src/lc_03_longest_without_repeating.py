"""[summary]

Returns:
    [type] -- [description]
"""

def solution(input_string):
    """
    :type s: str
    :rtype: int
    """

    ans = 0
    sub = ""
    for character in input_string:
        if character not in sub:
            sub += character
            ans = max(ans, len(sub))
        else:
            cut = sub.index(character)
            sub = sub[cut+1:] + character
    return ans
