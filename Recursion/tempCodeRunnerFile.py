  print("The Palindromic partitions are :-")
    print(" [ ", end="")
    for i in ans:
        print("[ ", end="")
        for j in i:
            print(j, end=" ")
        print("] ", end="")
    print("]")