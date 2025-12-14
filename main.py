def screen():
    '''
    Shuting Down
    '''
def screen2():
    '''
    Canciling shutdown
    '''
def shutdown(validation):
    if validation == "yes":
        print(screen.__doc__)
    elif validation == "no":
        print(screen2.__doc__)
    else:
        print("sorry")
validation = input("Proceed shutdown?:")
shutdown(validation)