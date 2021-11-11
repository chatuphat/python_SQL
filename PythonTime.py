print("startDate: 9:36:120")
print("endDate: 10:46:30")


startDate = "9:36:120"
endDate = "10:46:30"

startDate = startDate.split(":")
endDate   = endDate.split(":")


startHour = int(startDate[0])*3600
startMinute = int(startDate[1])*60
startSecond = int(startDate[2])
sumStart = (startHour+startMinute+startSecond)*0.016666


endHour = int(endDate[0])*3600
endMinute = int(endDate[1])*60
endSecond = int(endDate[2])
sumEnd =  (endHour+endMinute+endSecond)*0.016666



sumStartMinutes = round(sumStart,1)
sumEndMinutes = round(sumEnd,1)

print("SumDate: ",sumEndMinutes - sumStartMinutes ,"Minute")
