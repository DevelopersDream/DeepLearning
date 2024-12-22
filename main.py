import constants as c
import data_processing as dt
import utils as u

u.list_to_csv(file_name="sicilian_dataset", file_path=c.FINAL_DATASET,column_name="text",data=dt.full_data_processing())
