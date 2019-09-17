def main():
    height=int(input("Enter the height of the tree: "))
    h= height
    hashtag= 1
    while h >0:
        print(' ' * (h-1) + "#" * (hashtag))
        h -=1
        hashtag +=2
    print(" " * (height-1) + "#")
main()
