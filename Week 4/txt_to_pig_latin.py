'''
Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.
'''

def pig_latin(text):
  say = ""
  new_list = []
  i = 0
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    say = word[0]
    word = word[1:]
    word = word + say
    word = word + "ay"
    new_list.insert(i, word)
    i+=1
    # Turn the list back into a phrase
  return " ".join(new_list)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"