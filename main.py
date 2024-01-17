from schoolfilesystem import *

def main():
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


main()