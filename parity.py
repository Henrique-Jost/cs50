def main():
    x = int(input("Whats x?"))

    if is_even(x):
        print("It is Even")
    else:
        print("It is Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()

