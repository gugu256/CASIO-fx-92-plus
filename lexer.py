import math
from sys import argv



class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f"{self.token_type}:{self.value}"

def make_token(tok):
    if tok.startswith("(") and tok.endswith(")"):
        return Token("EXPR", tok)
    else:
        return Token(tok, None)

def purge(tokens):
    toks = []
    for tok in tokens:
        if tok == None:
            pass
        else:
            toks.append(tok)
    return toks

def lex(code):
    code += "\n"
    archaic_tokens = []
    tokens = []
    inexpr = False
    expr = ""
    incomment = False
    tok = ""

    for char in code:
        #print(char)
        if inexpr == False and incomment == False and char == "(":
            inexpr = True
            continue
        elif inexpr == True and incomment == False and char == ")":
            inexpr = False
            archaic_tokens.append("(" + expr + ")")
            expr = ""
            continue

        if inexpr:
            expr += char

        elif tok == "--":
            tok = ""
            incomment = True
        
        elif tok == "{" or tok == "}":
            archaic_tokens.append(tok)
            tok = ""

        elif incomment:
            tok = ""
            if char == "\n":
                incomment = False

        elif char in " \t\n":
            archaic_tokens.append(tok)
            tok = ""


        else:
            tok += char

    for token in archaic_tokens:
        tokens.append(make_token(token))

    return purge(tokens)

