import csv
from urllib.error import URLError, HTTPError
import pandas as pd
from urllib.request import urlopen

class SchoolAssessmentSystem:
    def __init__(self):
        self.assess_data = []

    def process_file(self, file_path):
        file_extension = file_path.split('.')[-1].lower()

        if file_extension == 'csv':
            with open(file_path, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.assess_data.append(dict(row))
                print(self.assess_data)
            return self.assess_data
        elif file_extension in ['xls', 'xlsx']:
            data = pd.read_excel(file_path)
            print(data)
            return data
        elif file_extension == 'txt':
            with open(file_path, 'r') as file:
                text = file.read()
                print(text)
        else:
            print(f"Unsupported file format: {file_extension}")         

    def transfer_data(self, source_file_path, destination_file_path):
        if source_file_path is None:
            print("No data found.")
            return
        file_extension = source_file_path.split('.')[-1].lower()

        if file_extension == 'csv':
            with open(destination_file_path, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=source_file_path[0].keys())
                writer.writeheader()
                for row in source_file_path:
                    writer.writerow(row)
        elif file_extension == 'txt':
            with open(destination_file_path, 'w') as file:
                for row in source_file_path:
                    file.write(str(row))
        elif file_extension in ['xlsx', 'xls']:
            df = pd.DataFrame(source_file_path)
            df.to_excel(destination_file_path, index=False)
        else:
            print("Invalid File.")
            return None
           

    def fetch_web_data(self, url):
        try:
            with urlopen(url) as response:
                source_data = response.read().decode('utf-8')
            return source_data
        except HTTPError as e:
            print(f"Error. {e}")
        except URLError as e:
            print(f"Error. {e}")
        except Exception as e:
            print(f"Error fetching. {e}")

    def analyze_content(self):
        #in process
        pass

    def generate_summary(self):
        #in process
        pass


school = SchoolAssessmentSystem()
school.process_file('lol.txt')
source_data = school.fetch_web_data(url='https://aupp.edu.kh')
print(source_data)