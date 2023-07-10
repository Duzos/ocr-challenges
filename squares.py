from util import * 

def printSquaresTilIdeal(max: int):
    current = 1

    compute_line(spin_amount=1,sleep_time=0.25)

    while current <= max:
        printSquare(current)
        time.sleep(0.1) # The delays are better than it being instant.
        current = current + 1

def printSquare(num: int):
    print(str(num) + " squared is " + str(square(num)))

def square(num: int):
    return num**2

def main():
    while True:
        num = int(input("Number: "))
        printSquaresTilIdeal(num)

if __name__ == "__main__":
    main()