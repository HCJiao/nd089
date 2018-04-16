mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You need to write several lines of code before the print statement.
week_sales = [mon_sales, tues_sales, wed_sales, thurs_sales, fri_sales]
week_sales_total = sum(int(sales) for sales in week_sales)
print("This week's total sales: "+str(week_sales_total))