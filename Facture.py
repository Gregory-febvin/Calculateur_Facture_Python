# Total Price / Start the other function for calculate the values / IN: Product Price | Product Number | TVA Number / OUT: nothing
def calculation(price, number, ammount_tva):
    product_price_tva = ProductPriceTVA(price, ammount_tva)
    total_price_tva = TotalPriceTVA(product_price_tva, number)
    total_price = TotalPrice(price, number)
    shipping_fees = ShippingCount(total_price)

    post_price(price, number, total_price, product_price_tva, total_price_tva, shipping_fees)
    
# Product Price with TVA / Calculate the price of the product with tva / IN: Product Price | TVA Number / OUT: Product Price with TVA
def ProductPriceTVA(price, ammount_tva):
    product_price_tva = tax_count(ammount_tva) * price
    return product_price_tva

# Total Price with TVA / Calculate the total price with tva / IN: Product Price with TVA | Number of Product / OUT: Total Price with TVA
def TotalPriceTVA(product_price_tva, number):
    total_price_tva = product_price_tva * number
    return total_price_tva

# Total Price / Calculate the total price / IN: Price | Number of Product / OUT: Total Price
def TotalPrice(price, number):
    total_price = price * number
    return total_price

# TVA Count / Calculate the tva / IN: TVA Pourcent / OUT: TVA Number (Between 0 and 1)
def tax_count(tva_pourcent):
    tva = tva_pourcent / 100 + 1
    return tva

# Shipping Count / Calculate the shipping fees / IN: Total Price / OUT: Shiping Fees
def ShippingCount(total_price):
    if total_price > 500:
        shipping_fees = "Free"
        return shipping_fees

    elif 100 < total_price < 500 :
        shipping_fees = total_price * 0.1
        return shipping_fees
    
    elif total_price < 100:
        shipping_fees = 10
        return shipping_fees

# Posting_Result / Print the result in the console / IN: Price | Number of Product | Total Price | Price Product with TVA | Total with TVA | Total without TVA | Shipping Fees / OUT: sentence
def post_price(price, number, total_price, product_price_tva, total_price_tva, shipping_fees):
    print("\nFacture : ")
    print("Product Price : {} | Number of Product : {}".format(price, number))
    print("Product Price with TVA : {} | Shipping Fees : {}".format(product_price_tva, shipping_fees))
    print("Total Ammount without TAX : {} | Total Ammount with TAX : {} \n".format(total_price, total_price_tva))

# Main / Let the user choose enter value and let him do another invoice / IN: Price | Number of product | TVA / OUT: nothing
while True:

    price_product = float(input("Pour commencer votre commande entrer le prix de votre produit : "))
    number_product = float(input("Maintenant entrer la quantite de produit souhaite : "))
    ammount_tva = float(input("Pour terminer veuillez indiquer le pourcentage de tva : "))

    
    total_price(price_product, number_product, ammount_tva)

    next_calculation = input("Une autre commande ? (oui/non): ")
    if next_calculation == "non":
        break
    else:
        print("Entré Invalide")