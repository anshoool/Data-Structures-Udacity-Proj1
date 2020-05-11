"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
time = {}
for duration in calls:
    if duration[0] in time:
        time[duration[0]] += int(duration[3])
    else:
        time[duration[0]] = int(duration[3])
    if duration[1] in time:
        time[duration[1]] += int(duration[3])
    else:
        time[duration[1]] = int(duration[3])

longestTime = max(time,key=lambda x:time[x])
print(str(longestTime)+" spent the longest time, "+str(time[longestTime])+" seconds, on the phone during September 2016")
