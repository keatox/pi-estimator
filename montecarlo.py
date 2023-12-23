import random
import matplotlib.pyplot as plt

def estimate(n):
    #calculates estimation of pi based on Monte Carlo integral and number of testcases
    inside_circle = 0
    x_out = []
    x_in = []
    y_out = []
    y_in = []
    for _ in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        sum = x**2 + y**2
        if sum <= 1:
            inside_circle += 1
            x_in.append(x)
            y_in.append(y)
        else:
            x_out.append(x)
            y_out.append(y)
    return [(4/n)*(inside_circle),x_in,y_in,x_out,y_out]

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
        ans = estimate(n)
        print(f'\nPI = {ans[0]}\n')
        #plots each generated coordinate and colors based on position in/out of circle
        plt.scatter(ans[1],ans[2],color='blue',s=50)
        plt.scatter(ans[3],ans[4],color="grey",s=50)
        plt.axis('square')
        plt.show()

if __name__ == "__main__":
    main()