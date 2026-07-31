def balanced_brackets(sequence):
    stack = []
    brackets = {")": "(", "}": "{", "]": "["}
    for bracket in sequence:
        if bracket in brackets.values():
            stack.append(bracket)
        elif bracket in brackets:
            if len(stack) == 0:
                return False
            if stack[-1] != brackets[bracket]:
                return False
            stack.pop()
    return len(stack) == 0

def main():
    sequence = "({[]})"
    if balanced_brackets(sequence):
        print("Esta balanceado")
    else:
        print("Esta desbalanceado")

main()