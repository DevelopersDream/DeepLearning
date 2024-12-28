import constants as c
import data_processing as dt
import utils as u

keep_shortgrams = False

if keep_shortgrams == False:
    file_name = "sicilian_dataset_less_shortgrams"
else:
    file_name = "sicilian_dataset"


u.list_to_csv(
    file_name=file_name,
    file_path=c.FINAL_DATASET,
    column_name="text",
    data=dt.full_data_processing(keep_shortgrams=keep_shortgrams),
)
