from datetime import datetime 

def billcalc(instpow):
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    
    avg_pow = instpow/currentDay
    monthly_usage = int(avg_pow*30)
    
    mylist = []
    rate = []
    for x in range(0,monthly_usage,50): 
        mylist.append(x)
        
    for u in range(0,len(mylist)):
        residue = monthly_usage - mylist[u]
        
    for i in mylist:
        if i <= 50:
            price = i*2.8
            rate.append(price)
        elif i > 50 and i <= 100:
            price = 50*3.2
            rate.append(price)
        elif i > 100 and i <= 150:
            price = 50*4.2 
            rate.append(price)
        elif i > 150 and i <= 200:
            price = 50*5.8 
            rate.append(price)
        else:
            price = 50*7
            rate.append(price)
            
   
    
    total=0
    for j in range(0,len(rate)):
        total = total + rate[j]
        
    final=0 
    if monthly_usage > 200:
        final = residue*7
    elif monthly_usage <= 200 and  monthly_usage > 150:
        final = residue*5.8
    elif monthly_usage <= 150 and monthly_usage > 100:
        final = residue*4.2
    elif monthly_usage <=100 and monthly_usage > 50:
        final = residue*3.2
    else:
        final=residue*2.8
        
    ulti = total+final
    
    
    print("estimated monthly usage :",monthly_usage)
    print("approximate monthly charge :",ulti)
    return monthly_usage,ulti
        
        
        
billcalc(200)
    
    








