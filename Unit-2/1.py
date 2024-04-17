try:
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    if b == 0:
        raise Exception("What are you doing, man?")
    print(f"a / b = {a/b}")
except Exception as e:
    print(f"Something went wrong. {e}")
print("End")
