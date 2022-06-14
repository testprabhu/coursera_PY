import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename,"w") as file:
    pass
  timestamp = os.path.getmtime(filename)
  #print(timestamp)
  # Convert the timestamp into a readable format, then into a string
  dt_object = datetime.date.fromtimestamp(timestamp)
  #print(dt_object)
  # Return just the date portion 

  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(dt_object))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd