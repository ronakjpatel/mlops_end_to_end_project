import os
from end_to_end_mlops import logger
from end_to_end_mlops.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    #this function simply checks the data file schema matches with the col names present in the schema.yaml file
    # if yes then sets the validation_status to TRUE otherwise FALSE. 
    #This function only checks the col names but you can also implement datatype checking logic as well if you are rigourous about data type as well. 
    
    def validate_all_columns(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            validation_status = all(col in all_schema for col in all_cols)

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e


