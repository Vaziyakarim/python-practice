# def fun():
#     print("Hello")
    
    
# print("start")
# fun()
# print("stopped")
# # EX-2
# def add(a,b):
#     return a+b
    
    
# print("added", add(5,6))
# print("added", add(6,6))
#EX-3
# def name(Fname,Lname):
#    print(f'{Fname} {Lname} Welcome')
 
 
# name("vaziya","karim")
# #Key Word Argument
# name(Fname="karim",Lname="vaziya")

# #Return Statements
# def sq(n):
#     return n*n
# print(sq(3))
def emojis(message):
        words=message.split(" ")
        emoji={
        ":)":"😃",
        ":(":"🙁"
        }
        output=""
        for word in words:
          output += emoji.get(word, word) + " "
        return output
 
 
message=input(">")
print(emojis(message))  

        