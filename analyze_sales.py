from collections import Counter, defaultdict
import csv
import os
import locale

#Funktion för att få rätt formaterad valuta
def format_currency(value):
    return locale.currency(value, grouping=True)

#Funktion för att ladda upp och öppna databasfilen 
def load_sales(filename):
    products = []
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader, start=1):
            row['ProductID'] = row.get('ProductID', str(i)) #ta från fil eller sätt löpnummer
            row['Sales'] = float(row['Sales'])
            products.append(row)
    return products
          
#Funktion för att analysera filen och ta reda på mest sålda och lukrativa produkter       
def analyze_sales_data(products):    
    sales_count = Counter()
    sales_sum = defaultdict(float)
    quantity_sum = defaultdict(int) #beräknar kvantitet
    sold_sum = defaultdict(int) #beräknar antal sålda
    product_names = {}
    #TODO: Hitta den mest sålda produkten (TIPS! Använd Counter från collections)
    
    for p in products:
        pid = p['ProductID']
        sales_count[pid] += 1
        sales_sum[pid] += p['Sales']
        quantity_sum[pid] += int(p['Quantity'])
        sold_sum[pid] += int(p['Sold'])
        if pid not in product_names: #tillåter flera namn
            product_names[pid] = p['Product']
    
    most_sold_id, most_sold_count = sales_count.most_common(1)[0]
    most_sold_name = product_names[most_sold_id]

    #TODO: Hitta den mest lukrativa produkten med max: max(products, key=products.get)
    most_lucrative_id = max(sales_sum, key=sales_sum.get)
    most_lucrative_name = product_names[most_lucrative_id]
    most_lucrative_value = sales_sum[most_lucrative_id]
    
    return (sales_sum, quantity_sum, sold_sum, product_names,
            (most_sold_id, most_sold_name, most_sold_count),
            (most_lucrative_id, most_lucrative_name, most_lucrative_value))

#BONUS UPPGIFT:
#FIXME: Redovisa mest sålda produkt här
#TODO: BONUS: kan du skapa en funktion som skriver ut rätt formaterad valuta istället för detta?
#Funktion för att printa ut resultat på ett finare sätt
def print_report(sales_sum, quantity_sum, sold_sum, product_names, most_sold, most_lucrative):
    print("\n--- Försäljningsrapport ---\n")
    print(f"{'ID':<5} {'Produkt':<15} {'Kvantitet':>10} {'Antal sålda':>12} {'Försäljning (kr)':>20}")
    print("-" * 65)
    
    for pid in product_names:
        print(f"{pid:<5} {product_names[pid]:<15} {quantity_sum[pid]:>7} {sold_sum[pid]:>10} {format_currency(sales_sum[pid]):>22}")
    
    print("\nMest sålda produkt:")
    print(f"    {most_sold[1]} (ID: {most_sold[0]}) - Antal: {most_sold[2]}")
    
    print("\nMest lukrativa produkt:")
    print(f"    {most_lucrative[1]} (ID: {most_lucrative[0]}) - Försäljning: {format_currency(most_lucrative[2])}\n")


# Sätt språkinställning till svenska (Sverige) används för att skriva ut formaterad valuta
def main():
    locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  
    os.system('cls')
    products = load_sales('sales_data.csv')
    sales_sum, quantity_sum, sold_sum, product_names, most_sold, most_lucrative = analyze_sales_data(products)
    print_report(sales_sum, quantity_sum, sold_sum, product_names, most_sold, most_lucrative)
    
if __name__ == "__main__":
    main()
