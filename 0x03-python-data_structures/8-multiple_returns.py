#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence[0]== "":
        first_char = None
        return (0, first_char)
    else:
        first_char = sentence[0]
        return (len(sentence), first_char)
