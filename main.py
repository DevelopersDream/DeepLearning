import constants as c
import data_processing as dt
import utils as u

# shortgrams: uni-grams, bi-grams
# keep_shortgrams = True => full dataset
# keep_shortgrams = False => partial or reduced dataset
# no_shortgrams = False => partial dataset
# no_shortgrams = True => reduced dataset

keep_shortgrams = False
no_shortgrams = True

if keep_shortgrams == False:
    file_name = "sicilian_dataset_partial"
    if no_shortgrams == True:
        file_name = "sicilian_dataset_reduced"
else:
    file_name = "sicilian_dataset"

train_data, test_data = dt.full_data_processing(keep_shortgrams=keep_shortgrams, no_shortgrams=no_shortgrams)

u.list_to_csv(file_name=file_name + "_train",file_path=c.FINAL_DATASET,column_name="text", data=train_data)

u.list_to_csv(file_name=file_name + "_test", file_path=c.FINAL_DATASET, column_name="text", data=test_data)
