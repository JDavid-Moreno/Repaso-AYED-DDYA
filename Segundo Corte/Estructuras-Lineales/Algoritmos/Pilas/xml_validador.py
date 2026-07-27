import re

def validate_xml(filename):
    stack = []
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    tags = re.findall(r"</?[a-zA-Z0-9]+>", content)
    for tag in tags:
        if tag.startswith("</"):
            name = tag[2:-1]
            if not stack:
                return False
            if stack.pop() != name:
                return False
        else:
            name = tag[1:-1]
            stack.append(name)
    return len(stack) == 0

def main():
    filename = "ejemplo.xml"
    print(validate_xml(filename))
main()