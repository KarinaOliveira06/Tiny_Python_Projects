def print_cart_matrix(shopping_cart):
    print("-------")
    
    if not shopping_cart:
        print("[ Empty ]")
    else:
        for l in range(len(shopping_cart)):
            for c in range(1):
                print(f"[{shopping_cart[l][c]}]")
                
    print("-------")