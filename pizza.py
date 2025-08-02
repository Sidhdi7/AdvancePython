def make_pizza(size,*topping):
    """Summarize the pizza we are about to make."""
    print(f"\n Making a{size}-inch pizza with the following toppings:")
    for topping in topings:
        print(f"-{topping}")