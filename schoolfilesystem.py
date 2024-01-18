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

        if source_file_path.endswith('csv'):
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
                print(source_data)
        except HTTPError as e:
            print(f"Error. {e}")
        except URLError as e:
            print(f"Error. {e}")
        except Exception as e:
            print(f"Error fetching. {e}")

    def analyze_content(self, data, filename):
        file_extension = filename.split('.')[-1].lower()
        
        if file_extension == 'csv':
            passCount = 0
            failCount = 0
            for i in range(len(data)):
                if float(data[i]["Overall"])>50:
                    passCount +=1
                else:
                    failCount +=1
            print(f"{passCount} students have Passed the Overall scores. {failCount} students have Failed the Overall scores.")
        else:
            print("No Analyzation found.")

    def generate_summary(self, data, filename):
        file_extension = filename.split('.')[-1].lower()

        if file_extension == 'csv':
            for i in range(len(data)):
                print(f"{data[i]['Last Name']} {data[i]['First Name']} With an ID of {data[i]['ID']} has an Overall of {data[i]['Overall']} and need improvements on {data[i]['Improvement']}.")
        else:
            print("No summary found.")

Options = input("Enter Number: 1=URL / 2=Filename: ")
school = SchoolAssessmentSystem()
if Options == "1":
    url = input("Enter the URL:")
    data = school.fetch_web_data(url)
elif Options == "2":
    filename = input("Enter the filename: ")
    data = school.process_file(file_path=filename)
    school.transfer_data(data, filename)
    school.analyze_content(data,filename)
    school.generate_summary(data, filename)
else:
    print('Invalid')