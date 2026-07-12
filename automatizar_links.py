import re

def front_page(link):
    match = re.search(r"watch\?v=([A-Za-z0-9_-]{11})", link)
    return match.group(1) if match else None

def main():
    link = input("Link: ")
    name = input("Name: ")
    front = front_page(link)
    print(f"[![{name}](https://img.youtube.com/vi/{front}/0.jpg)]({link})")

main()
