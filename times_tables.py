from util import * 

def printTimesTilIdeal(mult: int):
    current = 1

    compute_line(spin_amount=1,sleep_time=0.25)
    print("/n")

    while current <= 12:
        printTimes(current,mult)
        time.sleep(0.1) # The delays are better than it being instant.
        current = current + 1

def printTimes(num: int, num2: int):
    print(str(num) + " x " + str(num2) +" = "+ str(num*num2))

def main():
    while True:
        num = int(input("Number: "))
        printTimesTilIdeal(num)

if __name__ == "__main__":
    main()