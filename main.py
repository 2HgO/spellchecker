from textblob import TextBlob, Word
import os
from colorama import Fore, Style

class SpellCheck:
  '''Spell checker class that checks for errors in the spelling of words in the input file'''

  def __init__(self, filePath: str, maxSuggestions: int = 10):
    self.filePath = filePath
    self.maxSuggestions = maxSuggestions
    self.suggestions = []
  
  def checkwords(self):
    with open(self.filePath, 'r+') as file:
      for line in file:
        wordlist = TextBlob(line).words
        for word in range(len(wordlist)):
          check = wordlist[word].spellcheck()
          if len(check) == 0 or ( len(check) == 1 and wordlist[word] == check[0][0] ):
            continue
          else:
            wordlist[word] = [wordlist[word]] + [a for (a,b) in check if b >= 0.1]
        yield wordlist

  def cstrSolution(self):
    self.suggestions = []
    print("\n")
    count = 1
    for line in self.checkwords():
      errCount = 0
      print(f"{Fore.GREEN}Suggestions{Style.RESET_ALL} on line {Fore.BLUE}{count}{Style.RESET_ALL}:\n")
      for elem in line:
        if type(elem) == list:
          print(f"{Fore.RED}Error:{Style.RESET_ALL} {elem[0]}; {Fore.GREEN}Sugestions{Style.RESET_ALL}: {repr(elem[1:])}\n")
          errCount += 1
      if errCount == 0:
        print(f"{Fore.BLUE}{repr(None)}{Style.RESET_ALL}\n")
      count += 1

p = SpellCheck("tmp/mago.txt")
p.cstrSolution()      