import constants as c
import data_processing as dt
import plots as p
import utils as u

# my_data = dt.wiki_data_processing()

my_data = dt.books_data_processing()

for elem in my_data:
    
    print("\n\n" + elem[:500])

######

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
