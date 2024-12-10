import constants as c
import data_processing as dt
import plots as p
import utils as u

# my_data = dt.wiki_data_processing()

my_data = dt.books_data_processing()

# check unique characters besides letters and numbers
u.unique_characters(my_data)

# clean strings
import string

allowed_chars = string.ascii_letters + string.punctuation + string.digits + " " + "\n"
new_data = []

for input_string in my_data:

    new_data.append("".join(char for char in input_string if char in allowed_chars))


# check unique characters besides letters and numbers
u.unique_characters(new_data)

print(new_data[8][:10])

# p.token_distribution(my_data)


# for elem in data:
#  print(elem)


# for elem in data:
# print(elem["id"])

# data = [elem for elem in data if elem["title"] == "Tiatru"] #select a page based on the title

# text_list = [elem for elem in text_list if elem.count(" ")>0] #remove uni-grams

# for elem in text_list:
# print(elem.count(" "))
# print(elem)
