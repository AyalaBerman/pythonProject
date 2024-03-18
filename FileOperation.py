import pandas as pd
import numpy as np
import os
from Exception import Exceptions
from xml.dom.minidom import Document

exception_handler = Exceptions()
class FileOperation(object):
    def read_csv (self, file_path: str):
        try:
            data = pd.read_csv(file_path)
            print(data)
        except Exception as e:
            exception_handler.print(f"reading csv file was failed: {e}")

    def save_to_csv(self, data, file_name: str):
        try:
            if isinstance(data, pd.DataFrame):
                data.to_csv(file_name, index=False)
                print(f"Data saved to {file_name} successfully.")
                return True
            else:
                print("Invalid data type. Please provide a Pandas DataFrame.")
                return False
        except Exception as e:
            exception_handler.print(f"Saving data to excel file was failed: {e}")
            return False

    def read_file(self, file_path: str, type: str):
        try:
            if type.lower() == 'csv':
                return self.read_csv(file_path)
            elif type.lower() in ['excel', 'xls', 'xlsx']:
                return pd.read_excel(file_path)
            elif type.lower() in ['word', 'doc', 'docx']:
                doc = Document(file_path)
                return [p.text for p in doc.paragraphs]
            else:
                print(f"Unsupported file type: {type}")
                return None

        except FileNotFoundError as error:
            exception_handler.print(error)

        except Exception as e:
            exception_handler.print(e)









