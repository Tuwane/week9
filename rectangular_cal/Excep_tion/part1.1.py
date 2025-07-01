try:
    print(x)
except NameError:
    print("Varable x is not defined") 
except:
    print("Something else went wrong")
    
    
    x = -1
    
    if x < 0 :
        raise Exception("Sorry , no number bellow zero")       