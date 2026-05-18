from textnode import TextNode, TextType

def main():
    regNode = TextNode("this is some anchor text", TextType.IMAGE, "https://www.boot.dev")
    trueComp = TextNode("this is some anchor text", TextType.IMAGE, "https://www.boot.dev")
    falseComp = TextNode("gibberish", TextType.BOLD)

    print("Test representation output")
    print(regNode)
    print(f"Test if equality works w/ the same object: {regNode == trueComp}")
    print(f"Test if equality works w/ not the same object: {regNode == falseComp}")

if __name__ == "__main__":
    main()