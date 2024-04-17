try:
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    assert b != 0, "You can't devide number by zero"
    print(f"a / b = {a/b}")
except AssertionError as e:
    print(f"Something went wrong. {e}")
print("End")
