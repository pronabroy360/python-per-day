def main():
    n = 3
    prev = 1
    prev2 = 1

    for i in range(2, n+1):
        cur = prev + prev2
        prev2 = prev
        prev = cur
    print(cur)

if __name__ == "__main__":
    main()