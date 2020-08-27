# p="\nTo end this program press q"
# p += "\nenter your name"
# message = ""
# while message != "q":
#     message=input(p)
#     print(message)

a="hello my name is my name your name is my naem and my is my"
b=a.find("we",0)
while b!=-1:
    print(b)
    b=a.find("my",b+1)


x = "what we think we become; we are Python programmer"
y=x.find("we",0)
while y!=-1:
    print(y)
    y=x.find("we",y+1)