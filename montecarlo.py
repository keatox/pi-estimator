import random

def estimate(n):
    #calculates estimation of pi based on Monte Carlo integral and number of testcases
    inside_circle = 0
    for _ in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        sum = x**2 + y**2
        if sum <= 1:
            inside_circle += 1
    return (4/n)*(inside_circle)

def main():
    #requests value of n from user and prints estimation of pi
    n = None
    while n != 0:
        while True:
            try:
                print("Enter '0' to exit program.") 
                n = int(input("Enter number of testcases: "))
                if n >= 0:
                    break
                raise Exception
            except:
                print("\nEnter a positive integer.\n")
        if n == 0:
            print("\nExiting program.\n")
            break
        print(f'\nPI = {estimate(n)}\n')

if __name__ == "__main__":
    main()