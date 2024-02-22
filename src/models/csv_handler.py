"""
csv_handler.py

CSV File Handler. All necessary functions to handle csv files
"""

import csv


class CSVHandler():
    """
    CSV Handler
    """
    def __init__(self, file_path):
        """
        CSV Handler initializer

        Args:
            file_path: Path to csv file to work with
        """
        self.file_path = file_path

    def write_data(self, data):
        """
        Write data on csv file

        Args:
            data: Data to write on file
        """
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def get_data(self):
        """
        Reads csv file

        Returns:
            data: Data on file
        """
        data = []
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)

        return data
