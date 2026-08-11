def to24hourtime(hour, minute, period):
    # hour will always range from 1 to 12 (inclusive)
    # minute will always range from 0 to 59 (inclusive)
    # period will always be either "am" or "pm"
    time=''
    hr=''
    min=''
    a=0
    if minute<=9:
        min='0'+str(minute)
    elif minute>9:
        min=str(minute)
    if period is 'pm':
        a+=12
    if period is 'am' and hour<10:
        hr='0'
        
    if hour==12 and period=='am':
        hour=0
        hr='0'
    if hour==12 and period=='pm':
        hour=0
        hr=''
        
    time=hr+str(a+int(hour))+min
    return time
print(to24hourtime(12,3,'pm'))