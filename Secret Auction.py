from replit import clear
pairs={}
def info():
    name=input("Enter your name:")
    pairs[name]=int(input("Enter your bid:"))
    more=input("Are there any more bidders?")
    clear()
    return more
check='yes'
while(check=='yes'):
    check=info()
if(check=='no'):
    max=0
    for key in pairs:
        if(pairs[key]>max):
            max=pairs[key]
print(f"The highest bid is {max}")