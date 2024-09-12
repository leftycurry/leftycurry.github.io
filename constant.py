import math

def order(D, S, C, I, LT):
    try:
        # Calculate total cost and economic order quantity 
        numerator = 2 * D * S
        denominator = I * C
        Q_squared = numerator / denominator
        Q = math.sqrt(Q_squared)
        
        # Round up
        Q_up = math.ceil(Q)
        TC = (D / Q_up) * S + (I * C / 2) * Q_up

        # Calculate Reorder point quantity in units 
        R_square = (D / 52) * LT
        R_up = math.ceil(R_square)
        return R_up

        # Conclusion 
        message = f"When the inventory level drops to {R_up} units, place a replenishment order for {Q_up}."
        print(message)
        return message
