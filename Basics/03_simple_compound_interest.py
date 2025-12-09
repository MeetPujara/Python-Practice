# Find the simple interest and compound interest

principal = 10000
rate = 10
time = 5

simple_interest = (principal * rate * time)/100
total_amt = principal*(1+rate/100)**time
compound_interest = total_amt - principal
print(f"Simple Interest:",simple_interest)
print(f"Compound Interest:",compound_interest)