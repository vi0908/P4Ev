def add_time(start, duration, day = None):

   start_time = start.split(' ')
   ampm = start_time[1]
   start_hour = start_time[0].split(':')[0]
   start_minute = start_time[0].split(':')[1]
   count_day = 0
   

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

              if ampm == 'AM': 
                ampm = 'PM'

              else:
                ampm = 'AM'
                count_day +=1 
              
            else:
                sum_hours += 1

            sum_minutes = sum_minutes - 60
            end_minutes = str(sum_minutes)
   
   
   if  sum_hours <= 12:

        end_hour = str(sum_hours)

   else:
        while sum_hours >= 12:


            if ampm == 'AM':
                ampm = 'PM'
                
            else:
                ampm = 'AM'
                count_day += 1
                
            
            sum_hours = sum_hours - 12
            end_hour = str(sum_hours)

    

     
   if sum_hours == 0:
     end_hour = str('12')
     
   if int(end_minutes) <=9:
       end_time = end_hour + ':' + '0' + end_minutes + ' ' + ampm

   else:
       end_time = end_hour + ':' + end_minutes + ' ' + ampm



   if count_day == 1:
        end_day = (" (next day)")
     
   elif count_day < 1:
       end_day = ''

   else:
        end_day = " (" + str(count_day) + " days later)"



   if day is not None:

       day = day.lower().capitalize()
       days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday':6}
       start_day = days.get(day)
       duration_day = start_day + count_day

       while duration_day > 7:
           duration_day -=7

       final_day = list(days.keys())[duration_day]
       print (final_day)
        







   return end_time 

print(add_time("11:59 PM", "0:05", "Wednesday"))