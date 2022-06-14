import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  f = open(filename, "x")
  with open (filename) as file:
    pass
  current_dir = os.getcwd()
  #print(os.getcwd())
  # Return the list of files in the new directory
  return os.listdir(current_dir)

print(new_directory("PythonPrograms", "script.py"))