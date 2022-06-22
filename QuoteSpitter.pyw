from win10toast import ToastNotifier
import time
import random

# empty list to store quotes from file
quotes = []

# open and add all quotes to list by line
f = open(r'C:\Users\andre\Desktop\quotes.txt', 'r')
for line in f:
    quotes.append(line)

# show given quote as notification
def showNotif(quote):
    toast = ToastNotifier()
    toast.show_toast("Quote Spitter", quote, duration = 15)

# choose random quote and call showNotif function, then sleep
while True:
    showNotif(random.choice(quotes))
    time.sleep(1200)
