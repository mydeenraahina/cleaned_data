from requests import get
import pandas as pd

# URLs for the Excel files
url1 = "https://raw.githubusercontent.com/mydeenraahina/data_set/master/Electors Data Summary.xlsx"
url2 = "https://raw.githubusercontent.com/mydeenraahina/data_set/master/PoliticalParties_ContestedSeats.xlsx"
url3 = "https://raw.githubusercontent.com/mydeenraahina/data_set/master/party performance.xlsx"

# Local file names to store the downloaded Excel files
file_1 = "Electors Data Summary.xlsx"
file_2 = "PoliticalParties_ContestedSeats.xlsx"
file_3 = "party performance.xlsx"

class Read_Data():
    # Setting display options for Pandas
    pd.options.display.max_rows = 150
    pd.options.display.max_columns = 8

    @staticmethod
    def Read_Excel(url, file_name):
        try:
            # Sending a GET request to the URL to retrieve the file content
            retrieve = get(url)

            # Opening the local file in binary write mode and writing the content
            with open(file_name, 'wb')as file:
              file.write(retrieve.content)

            # Reading the Excel file using pandas
            dataset = pd.read_excel(file_name)
        except FileNotFoundError as e1:
            # Print an error message if the file is not found
            print(f"Error: {e1} File not found")
        else:
            # Return the dataset if successfully read
            return dataset
# Dataset 1: Electors Data Summary
dataset1 = Read_Data.Read_Excel(url1,file_1)
# Dataset 2: PoliticalParties_ContestedSeats
dataset2 = Read_Data.Read_Excel(url2,file_2)
# Dataset 3: Performance of Political Parties
dataset3 = Read_Data.Read_Excel(url3,file_3)
# Cleaning dataset1-Electors Data
class Clean_Dataset1:

    def removing_empty_val(self, dataset):
        # Removing empty values
        dataset.dropna(inplace=True)

    def removing_duplicates(self, dataset):
        # Removing duplicate values
        dataset.drop_duplicates(inplace=True)

    def setting_index(self, dataset):
        # Setting 'Election-related metrics' as the index
        index_name = 'Election-related metrics'
        dataset.set_index(index_name, inplace=True)

    def cleaned_data(self, dataframe):
        # Create a copy to avoid modifying the original DataFrame
        dataset = dataframe

        # Apply cleaning steps

        self.removing_empty_val(dataset)
        self.removing_duplicates(dataset)
        self.setting_index(dataset)

        # Return the cleaned dataset
        return dataset


cleaned_dataset1=Clean_Dataset1()
dataset1_cleaned=cleaned_dataset1.cleaned_data(dataset1)
print(f"{dataset1_cleaned}")

# Cleaning dataset2 - PoliticalParties_ContestedSeats
class Clean_Dataset2:

    def droping_cols(self, dataset):
        # List of columns dropped from the DataFrame
        drop_columns = ["WON", "VOTES", "PERCENTAGE", "FD"]
        # Drop the specified columns
        dataset.drop(columns=drop_columns, inplace=True)

    def rename_cols(self, dataset):
        # Rename the column "ABBREVIATION" to "POLITICAL_PARTIES"
        dataset.rename(columns={"ABBREVIATION": "POLITICAL_PARTIES"}, inplace=True)

    def removing_empty_val(self, dataset):
        # Use the removing_empty_val method from Clean_Dataset1 to remove empty values
        cleaned_dataset1.removing_empty_val(dataset)

    def removing_duplicates(self, dataset):
        # Use the removing_duplicates method from Clean_Dataset1 to remove duplicate rows
        cleaned_dataset1.removing_duplicates(dataset)

    def setting_index(self, dataset):
        # Setting 'POLITICAL_PARTIES' as the index
        dataset.set_index('POLITICAL_PARTIES', inplace=True)

    def cleaned_data(self, dataset):
        # Apply cleaning steps
        self.droping_cols(dataset)
        self.rename_cols(dataset)
        self.removing_empty_val(dataset)
        self.removing_duplicates(dataset)
        self.setting_index(dataset)
        return dataset

# Create an instance of Clean_Dataset2
cleaned_dataset2 = Clean_Dataset2()

# Clean the dataset using the Clean_Dataset2 class
dataset2_cleaned = cleaned_dataset2.cleaned_data(dataset2)
print(f"{dataset2_cleaned}")

# Cleaning dataset3 - Performance of Political Parties
class Clean_Dataset3:
    def drop_cols(self, dataset):
        # Drop the 'FD' column as it doesn't contribute to the analysis
        dataset.drop(columns="FD", inplace=True)

    def rename_cols(self, dataset):
        # Rename columns
        dataset.rename(columns={"ABBREVIATION":"PARTIES","VOTES": "TOTAL_VOTES", "%": "PERCENTAGE OF TOTAL_VOTES"}, inplace=True)

    def removing_empty_val(self, dataset):
        # Drop rows with missing values
        cleaned_dataset1.removing_empty_val(dataset)

    def removing_duplicates(self, dataset):
        # Drop duplicate rows from the DataFrame
        cleaned_dataset1.removing_duplicates(dataset)

    def setting_index(self, dataset):
        # Set 'PARTIES' column as the index
        dataset.set_index('PARTIES', inplace=True)

    def cleaned_data(self, dataset):
        # Apply cleaning steps
        self.drop_cols(dataset)
        self.rename_cols(dataset)
        self.removing_empty_val(dataset)
        self.removing_duplicates(dataset)
        self.setting_index(dataset)
        return dataset

# Create an instance of Clean_Dataset3
cleaned_dataset3 = Clean_Dataset3()
# Clean the dataset using the Clean_Dataset3 class
dataset3_cleaned = cleaned_dataset3.cleaned_data(dataset3)
print(f"{dataset3_cleaned}")