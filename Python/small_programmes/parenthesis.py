from stack import Stacks

def balance(brackets):
    n = len(brackets)
    hold = Stacks()

    for i in range(n):
        if brackets[i] == '(':
            hold.push(brackets[i])
        elif brackets[i] == ')':
            if len(hold) == 0:
                return False
            else:
                hold.pop()

    if len(hold) == 0: return True
    else:return False

def reverse_string(string):
    word = Stacks()
    for letters in string:
        word.push(letters)

    reverse = ""
    for _ in range(len(word)):
        reverse += word.pop()

    return reverse

if __name__ == '__main__':
    eg1 = '(()())'
    eg2 = '(()'
    print("*"*50)
    print(f'Is (()()) balanced? {balance(eg1)}')
    print(f'Is (() balanced? {balance(eg2)}')

    word = "hello"
    print(reverse_string(word))