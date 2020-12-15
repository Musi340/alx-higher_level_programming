#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    else:
        l = len(sentence)
        f = sentence[0]
        return (l, f)
