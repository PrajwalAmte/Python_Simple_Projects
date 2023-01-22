import pyshorteners

link = input("Enter the link: ")   # variable
shortener = pyshorteners.Shortener()   # class object

x = shortener.tinyurl.short(link)   # shortening the link
print(x)