weight=int(input('Enter weight : '))
unit=input(" '(' L ')' bs or '(' K')' g: ")
if unit.upper() == "L":
 weight_k=weight * 0.453592
 print('The weight in kgs : ', weight_k)
else:
    weight_k=weight/0.453592
    print('The weight in pounds : ', weight_k)
    
    
