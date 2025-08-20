# Program to calculate Profit or Loss and their percentages

# Input cost price and selling price
cost_price = float(input("Enter Cost Price (CP): "))
selling_price = float(input("Enter Selling Price (SP): "))

# Calculate Profit or Loss
if selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percent = (profit / cost_price) * 100
    print(f"Profit: {profit:.2f}")
    print(f"Profit Percentage: {profit_percent:.2f}%")
elif selling_price < cost_price:
    loss = cost_price - selling_price
    loss_percent = (loss / cost_price) * 100
    print(f"Loss: {loss:.2f}")
    print(f"Loss Percentage: {loss_percent:.2f}%")
else:
    print("No Profit, No Loss")
