# Task 1

def calculate_price(quantity,price):
    total_price = quantity * price
    discount = 0.1     

    def apply_discount (price):
       
        discouned_price = price * (1-discount)
        return discouned_price

    discounted_total_price = apply_discount (total_price)
    return discounted_total_price

def main():
    quantity = 2
    price = 5
    result = calculate_price(quantity, price)
    print(result)  

if __name__ == "__main__":
    main()


# Local Variables is discouned_price  
# Enclouser is discount  ,total_price    
# there is no Globale varible 
 


