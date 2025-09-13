customer={
   "name":"vaziya",
    "sen":47,
    "is_verified":True
}
print(customer["name"])
#get ,if error it give  none
print(customer.get("name"))
print(customer.get("birthday","17"))
#or
customer["birthday"]="feb 17"
print("birthday")

#Changing
customer["name"]="vazz"
print(customer["name"])

# Ex:2
phone=input("phone:")
translate={
    "1":"one",
    "2":"two",
    "3":"three"
}
output=""
for check in phone:
  output +=  translate.get(check,"!") +  " "
print(output)

#EX:3
enter=input(">")
words=enter.split(' ')
emoji={
    ":)":"😃",
    ":(":"🙁"
}
output=""
for word in words:
   output += emoji.get(word, word) + " "
print(output)