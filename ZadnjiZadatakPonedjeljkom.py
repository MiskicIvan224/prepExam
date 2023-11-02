


import csv
def file_name(filename,column):
    counter = 0
    gradeAVG = 0
    with open (filename) as file:
        
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for line in csv_reader:
            grades = line[column]
            try:
                counter += float(line[column])
                
                gradeAVG+=1
            except ValueError:
                print("skipped")
        print(counter/gradeAVG)

def main():

    filename = ("data/full_grades_010a.csv")

    for column in range(3,13):
        file_name(filename,column)



if __name__ == "__main__":
    main()