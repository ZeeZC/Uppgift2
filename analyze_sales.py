from collections import Counter
import csv
import os
import locale

#Funktion för att få rätt formaterad valuta
def format_currency(value):
    return locale.currency(value,grouping=True)

#Funktion för att ladda upp och öppna databasfilen 
def load_sales(filename):
    products = {}
    all_products = []
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = row['Product']
            sales = float(row['Sales'])
            
            all_products.append(product)
            
            if product in products:
                products[product] += sales
            else:
                products[product] = sales
                
    return all_products, products
          
#Funktion för att analysera filen och ta reda på mest sålda och lukrativa produkter       
def analyze_sales_data(all_products, products):    
    print(products)
    #TODO: Hitta den mest sålda produkten (TIPS! Använd Counter från collections)
    
    most_sold = Counter(all_products)
    most_common_product = most_sold.most_common(1)[0]
    print(most_sold)
    
    #TODO: Hitta den mest lukrativa produkten med max: max(products, key=products.get)
    most_lucrative_product = max(products, key=products.get)
    product_value = products[most_lucrative_product]
    
    print(f"Mest sålda produkt: {most_common_product[0]}, Antal: {most_common_product[1]}")  #FIXME: Redovisa mest sålda produkt här
    print(f"Mest lukrativa produkt: \"{most_lucrative_product}\" med försäljning på {format_currency(product_value)}") #TODO: BONUS: kan du skapa en funktion som skriver ut rätt formaterad valuta istället för detta?


# Sätt språkinställning till svenska (Sverige) används för att skriva ut formaterad valuta
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

os.system('cls')
all_products, products = load_sales('sales_data.csv')
analyze_sales_data(all_products, products)
