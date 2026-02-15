from stack import Stacks

def infix_to_postfix(eq):
    num = ""
    op = Stacks()
    out = Stacks()
    s = 'word'

    operators = {'^' : 1,'/' : 2,'*' : 3,'+' : 4,'-' : 5}
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    
    for it in eq:
        if it.isalnum():
            out.push(it)
        elif it == "(":
            op.push(it)
        elif it == ")":
            pass

## Needs fixing
        