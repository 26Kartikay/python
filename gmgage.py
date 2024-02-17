import time
timestamp=(time.strftime('%H:%M:%S'))
print(timestamp)
hour=int(time.strftime('%H'))
min=int(time.strftime('%M'))
sec=int(time.strftime('%S'))
if (hour >=4 and hour <12):
    print("GOOD MORNING :)")
elif(hour>=12 and hour <20):
    print("GOOD EVENING :)")
else:
    print("GOOD NIGHT :)")