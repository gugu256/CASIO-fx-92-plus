import math
from sys import argv

varz = list("ABCDEFMxy")

funcs = [
    "forward",
    "turn",
    "orient",
    "goto",
    "pendown",
    "penup",
    "var",
    "input",
    "say",
    "showresult",
    #"style",
    #"wait",
    "times",
    "until",
    "if",
    "else"
]

msgs = {
    "yes": "Yes",
    "no": "No",
    "ask": "Number : ",
    "result": "Result : "
}

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f"{self.token_type}:{self.value}"

def make_token(tok):
    if tok.startswith("(") and tok.endswith(")"):
        return Token("EXPR", tok)
    elif tok == "{":
        return Token("LCURL", None)
    elif tok == "}":
        return Token("RCURL", None)
    elif tok in varz:
        return Token("VARNAME", tok)
    elif tok in funcs:
        return Token(tok.upper(), None)
    elif tok in list(msgs.keys()):
        return Token("MSG", msgs[tok])
    else:
        return Token(tok, None)

def purge(tokens):
    toks = []
    for tok in tokens:
        if tok == None or tok == "":
            pass
        else:
            toks.append(tok.replace(" ", "")) if make_token(tok).token_type != "EXPR" else toks.append(tok)
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
            tok += char

        elif incomment:
            tok = ""
            if char == "\n":
                incomment = False

        elif char in " \t\n":
            archaic_tokens.append(tok)
            tok = ""
        
        elif char == "}":
            archaic_tokens.append(tok)
            tok = "}"


        else:
            tok += char

    for token in purge(archaic_tokens):
        tokens.append(make_token(token))

    return tokens

