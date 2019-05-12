import csv

a='\\Users\\owner\\Downloads\\Pybank_Resources_budget_data.csv'
b='\\Users\\owner\\Downloads\\budget_output.txt'
pl=[]
pl_summary={}

with open(a, newline='') as csvfile:
    
    budget_reader=csv.reader(csvfile,delimiter=',')
    next(budget_reader)
    total=0
    total_months=0
    
    for line in budget_reader:
        pl.append(line)
        total+=int(line[1])
        total_months+=1
       
    sm=0
    tm=0
    am=0
    max_decrease=int(pl[total_months-1][1])-int(pl[total_months-2][1])
    max_increase=int(pl[total_months-1][1])-int(pl[total_months-2][1])
   
    for i in range(total_months,1,-1):
        sm=int(pl[i-1][1])-int(pl[i-2][1])
        
        if sm < max_decrease:
            min_month_yr=pl[i-1][0]
            max_decrease=sm
        elif sm > max_increase:
            max_increase=sm
            max_month_yr=pl[i-1][0]
        
        tm=tm+sm
   
    am=tm/(total_months-1)
        
'''
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
'''
text_file=open(b,"w")
text_file.write('Financial Analysis')
print('Financial Analysis')
text_file.write('\n----------------------------')
print('----------------------------')
text_file.write('\nTotal Months: '+str(total_months))
print('Total Months: '+str(total_months))
text_file.write('\nTotal: $'+str(total))
print('Total: $'+str(total))
text_file.write('\nAverage  Change: $'+str(round(am,2)))
print('Average  Change: $'+str(round(am,2)))
text_file.write('\nGreatest Increase in Profits: '+max_month_yr+' ($'+str(max_increase)+')')
print('Greatest Increase in Profits: '+max_month_yr+' ($'+str(max_increase)+')')
text_file.write('\nGreatest Decrease in Profits: '+min_month_yr+' ($'+str(max_decrease)+')')
print('Greatest Decrease in Profits: '+min_month_yr+' ($'+str(max_decrease)+')')
text_file.close()
