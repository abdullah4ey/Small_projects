def strin_refiner(String):
    no_of_hash = String.count('#')
    #count the number of hash sign to limit the while loop
    while no_of_hash > 0:
        Index_no = String.find("#")
        if Index_no == 0:
            String = String[0 : Index_no : ] + String[Index_no + 1 : :]
            no_of_hash = no_of_hash-1
        else:
            String = String[0 : Index_no -1  : ] + String[Index_no + 1 : :]
            no_of_hash = no_of_hash-1
    else:
        print (String)    
strin_refiner("#Stringb#")
