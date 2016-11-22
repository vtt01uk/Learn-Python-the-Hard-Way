def break_words(stuff):
   """This function will break up words for us."""
   words = stuff.split(' ')
   return words

def sort_words(words):
   """Sorts the words."""
   return sorted(words)

def print_first_word(words):
   """Print the first word after popping it off."""
   word = words.pop(0)
   print word

def print_last_word(words):
   """Prints the last word after popping it off."""
   word = words.pop(- 1)
   print word

def sort_sentence(sentence):
   """Takes in a full sentence and return the sorted words."""
   words = break_words(sentence)
   return sort_words(words)

def print_first_and_last(sentence):
   """Prints the first and last words of the sentence."""
   words = break_words(sentence)
   print_first_word(words)
   print_last_word(words)

def print_first_and_last_sorted(sentence):
   """Sorts the words then prints the first and last one."""
   words = sort_sentence(sentence)
   print_first_word(words)
   print_last_word(words)

print "Let's practice everything."
print 'You\'d need to know \'about escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "------------------"
print poem
print "------------------"

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
  jelly_beans = started * 500
  jars = jelly_beans / 1000
  crates = jars / 100
  return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

started = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)

#sentence = "All good things come to those who wait."

#words = ex26.break_words(sentence)
#sorted_words = ex26.sort_words(words)

#ex26.print_first_word(words)
#ex26.print_last_word(words)
#ex26.print_first_word(sorted_words)
#ex26.print_last_word(sorted_words)
#sorted_words = ex26.sort_sentence(sentence)
#print sorted_words

#print_first_and_last(sentence)
#print_first_and_last_sorted(sentence)

