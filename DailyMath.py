#print("hello world")
#save money monthly and caculate the effective year interest rate
MonthFund = int(input("Please text the number of month fund : "))
TimeYear = int(input("Please input the number of years : "))
TimeMonth = TimeYear * 12
#ReturnRate = int(input("please input the return rate without %"))
GuessRate = float(input("Please guess the return year rate and expressed in decimals : "))
GuessRateMonth = GuessRate / 12
s = float(0)

for i in range(TimeMonth):
    #print(i)
    s = s + MonthFund * (1+GuessRateMonth)**(i+1)
print("Total investment in the end : ",round(s,2))
Total = MonthFund * TimeMonth
print("Total original investment : ", Total)
print("Asset ratio : ", round(s/Total,2), "times")