principal = float(input("Principal (without currency sign): "))
int_rate = float(input("Annual nominal interest rate (without percentage): "))/100
times_comp = float(input("Number of times interst is compounded per year: "))
years = float(input("Number of years: "))
int = principal*(1 + int_rate/times_comp)**(times_comp*years) - principal
print(int)
