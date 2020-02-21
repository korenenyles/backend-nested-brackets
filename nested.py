#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "SEAN BAILEY, CHRIS WILSON, KANO MARVEL "

import sys

def is_matched(s):
    brac_types = {       
        "parasts": ["(*", "*)"],
        "parens": ["(", ")"],        
        "squares": ["[", "]"],        
        "curlies": ["{", "}"],       
        "alligators": ["<", ">"]
    }
    
    opn_bracket = []
    index = 0    
    answer = "YES"

    while s:
        index += 1
        if s[:2] == '(*' or s[:2] == '*)':
            token = s[:2]
        else: 
            token = s[0]
        
        for brac in brac_types:
            if token == brac_types[brac][0]:
                opn_bracket.append(token)
            if token == brac_types[brac][-1]:
                if opn_bracket[-1] != brac_types[brac][0]:
                    answer = "NO " + str(index)
                    token = s 
                else:
                    opn_bracket.pop() 
        s = s[len(token):]
        
    if len(opn_bracket) > 0:
        answer = "NO " + str(index)
    return (answer)


            
            



   

def main(args):
    """Open the input file and call `is_nested()` for each line"""
    linecount = 0
    answer = ''
    with open('input.txt', 'r') as f:
        for s in f:
            answer += is_matched(s) + '\n'
            linecount += 1
    with open('output.txt', 'w') as f:
        f.write(answer)

if __name__ == '__main__':
    main(sys.argv[1:])