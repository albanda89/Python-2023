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



# Local Variables =  discount  ,total_price  and discouned_price 
# Enclouser is   
# there is no Globale varible 
 


