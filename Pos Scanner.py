wake = str(input("Press Enter to Continue... "))


ask = int(input("Input # of Items at Checkout: "))
price_numbers = 0
prices = 0
for number_of_items in range(1, ask + 1):
    print(f"{number_of_items}. ${(price_numbers := float(input(f"Price in $: $")))}")

    if number_of_items != ask+1:

        price_numbers_total = price_numbers
        prices += price_numbers

        if number_of_items != ask + 1:
            continue

print_total = input("Total? ")

if "y" or "yes" or "total" or "continue" in print_total.lower():
    print(f"Total: {prices}")
    print("Printing Receipt................")
