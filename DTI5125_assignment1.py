import nltk
import re
import random
from nltk import ngrams
import pandas as pd

nltk.download('gutenberg')

glutenberg_books = nltk.corpus.gutenberg.fileids()

print("These are the books from gutenberg project: ")
for book in glutenberg_books:
  print(book)

str_input = "how many books do you want between 1 and " + str(len(glutenberg_books)) + ": "
while True:
  try:
    n=int(input(str_input))
    if n not in [i+1 for i in range(len(glutenberg_books))]:
      raise ValueError()
    else:
      break
  except ValueError:
    print("Oops!  That was no valid number.  Try again between 1 and", len(glutenberg_books))


print("please select which book you want by the number")
for index, val in enumerate(glutenberg_books):
  print("for ",val, "select: ", index+1)

book_list = []
for i in range(n):
  while True:
    try:
      book_number = int(input())
      if book_number in book_list:
        raise ValueError()
      if book_number not in [i+1 for i in range(len(glutenberg_books))]:
        raise ValueError()
      book_list.append(book_number)
      break
    except ValueError:
      print("eithe this book you have entered have been already or you have given a wrong input, please provide input between 1 and", len(glutenberg_books))

print("These are the books that you have ordered for: ")
for book in book_list:
  print(glutenberg_books[book-1])

flag = True

while True:
  try:
    flag_i = int(input("Please choose how you want to partition, do you want to partition words randomly (press 1) or you want to partition by a chunks of the book (press 2)"))
    if flag_i not in [1, 2]:
      raise ValueError()
    else:
      break
  except ValueError:
    print("Oops!  That was no valid number.  Try again between 1 and 2")

if flag_i == 2:
  print("great! books will now be partitioned randomly in chunks or part of the text")
  flag = False
else:
  print("great! books will now be partitioned randomly and the words will also be picked randomly")

d = {}
if flag == False:

    for book in book_list:
        partitions = []
        file = nltk.Text(nltk.corpus.gutenberg.words(glutenberg_books[book - 1]))  # selecting the book

        file = [w.lower() for w in file if w.isalpha()]  # removing all symbols

        n = 100
        n_grams = list(ngrams(file, n))
        for i in range(200):

            sample_list = []

            for i in range(100):
                sample_list.append(n_grams.pop(random.randint(0, len(n_grams) - i)))

            partition = " ".join(sample_list[99])
            partitions.append(partition)

        book_name = glutenberg_books[book - 1]
        book_name = book_name.rsplit('.', 1)[0]
        d[book_name] = partitions

if flag == True:
    for book in book_list:
        partitions = []

        file = nltk.corpus.gutenberg.words(glutenberg_books[book - 1])
        file = list(file)

        words = [w.lower() for w in file if w.isalpha()]

        for i in range(200):
            a = []
            for j in range(100):
                index = random.randrange(0, len(words))
                a.append(words.pop(index))
            partition = " ".join(a)
            partitions.append(partition)

        book_name = glutenberg_books[book - 1]
        book_name = book_name.rsplit('.', 1)[0]
        d[book_name] = partitions

df = pd.DataFrame(d)
df.to_csv('gutenberg_books_processed.txt', encoding='utf-8', index=False, sep=',')