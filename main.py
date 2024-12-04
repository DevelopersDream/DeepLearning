import constants as c
import utils as u


data = u.one_json()


data = data[1:] #first document is not in sicilian, TODO also some other...

dataset_statistics = u.compute_init_dataset_stats(data)

doc_list = []

for elem in data: #data pre-processing and cleaning

    doc_list.append([elem["title"].lower()])  # no /n in titles, converting the single string in a list

    if elem["text"] != "":
        doc_list.append(elem["text"].lower().split("\n")) # a different docuemnt for every /n

doc_list = [item for sublist in doc_list for item in sublist] #list of lists -> list

del data

dataset_statistics = u.compute_final_dataset_stats(dataset_statistics, doc_list)

print(dataset_statistics)



# for elem in data:
#  print(elem)


# for elem in data:
# print(elem["id"])

# data = [elem for elem in data if elem["title"] == "Tiatru"] #select a page based on the title

# text_list = [elem for elem in text_list if elem.count(" ")>0] #remove uni-grams

# for elem in text_list:
# print(elem.count(" "))
# print(elem)
