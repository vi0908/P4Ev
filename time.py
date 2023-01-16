def add_time(start, duration, day = None):

   start_time = start.split(' ')
   ampm = start_time[1]
   start_hour = start_time[0].split(':')[0]
   start_minute = start_time[0].split(':')[1]

   duration_time = duration.split(':')
   duration_hour = duration_time[0]
   duration_minute = duration_time[1]

   sum_hours = int(start_hour) + int(duration_hour)
   sum_minutes = int(start_minute) + int(duration_minute)


   if sum_minutes < 60:
       end_minutes = str(sum_minutes)

   else:
        while sum_minutes >= 60:
            if sum_hours == 11:
              sum_hours += 1
            else:
                sum_hours += 1
                if ampm == 'AM': 
                    ampm = 'PM'
                else:
                    ampm = 'AM'

            sum_minutes = sum_minutes - 60
            end_minutes = str(sum_minutes)
   

   if  sum_hours <= 12:
        end_hour = str(sum_hours)
   else:
        while sum_hours > 12:
            
            if ampm == 'AM':
                ampm = 'PM'
            else:
                ampm = 'AM'
            
            sum_hours = sum_hours - 12
            end_hour = str(sum_hours)

   if int(end_minutes) <=9:
       end_time = end_hour + ':' + '0' + end_minutes + ' ' + ampm

   else:
       end_time = end_hour + ':' + end_minutes + ' ' + ampm

   return end_time
    
print(add_time("11:40 AM", "0:25"))


     





   
   
   

# Returns: 6:10 PM