def validate_pin(pin):

    return len(pin) in (4, 6) and pin.isdigit()

print(validate_pin('a300'))


""" Efforts:
def validate_pin(pin):
    try:
        if len(int(pin))==4 or len(int(pin))==6:
            print(pin)
            for i in pin:
                try:
                    if int(i)== True:
                        print(i)
                        return True
                except:
                    return False
            return True
    except:
        print('ex')
        return False
    else:
        return False
print(validate_pin('1300'))"""