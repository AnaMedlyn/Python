def print_tree(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

def main():
    tree_height = int(input("Digite a altura da árvore: "))
    print_tree(tree_height)

if __name__ == "__main__":
    main()
