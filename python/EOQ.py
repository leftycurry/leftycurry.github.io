import math

def main():
    print("Please enter the following variables:")
    
    try:
        D = float(input("D (Demand): "))
        S = float(input("S (Cost per order): "))
        C = float(input("C (Cost per item): "))
        I = float(input("I (Inventory holding cost): "))
        
        # Calculate Q using the formula Q = sqrt(2DS / (IC))
        numerator = 2 * D * S
        denominator = I * C
        
        if denominator == 0:
            print("The denominator is zero. Please check your inputs for C and I.")
            return
        
        Q_squared = numerator / denominator
        
        if Q_squared < 0:
            print("No real solution for Q. The value is negative.")
            return
        
        Q = math.sqrt(Q_squared)
        
        # Round up the result
        Q_rounded_up = math.ceil(Q)
        
        # Calculate Total Cost (TC)
        TC = (D / Q_rounded_up) * S + (I * C / 2) * Q_rounded_up
        
        # Conclusions
        print(f"Your economic order quantity will be: {Q_rounded_up}")
        print(f"Your total inventory cost will be: {TC:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
