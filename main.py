from schoolfilesystem import *

def main():
    Options = input("Enter Number: 1=URL / 2=Filename: ")

    if Options == "1":
        url = input("Enter the URL:")
        data = SchoolAssessmentSystem.fetch_web_data(url)
    elif Options == "2":
        filename = input("Enter the filename: ")
        data = SchoolAssessmentSystem.process_file(file_path=filename)
        SchoolAssessmentSystem.transfer_data(data, filename)
        SchoolAssessmentSystem.analyze_content(data,filename)
        SchoolAssessmentSystem.generate_summary(data, filename)
    else:
        print("Invalid")

main()