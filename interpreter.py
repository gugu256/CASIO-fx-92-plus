# An interpreter for the programming language contained in CASIO fx-92+ calulators
#
# Written by gugu256

import lexer

def repl():
    while True:
        print(lexer.lex(input(">>> ")))

repl()