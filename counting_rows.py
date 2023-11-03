import csv

def counting_rows(filename):
    
    with open (filename) as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for line in csv_reader:
            counter = 0
            class_average = 0.0
            for grade in line[3:13]:
                counter+=1
                try:
                    class_average+= float(grade)
                except ValueError:
                    print("ignored")
            print(class_average / counter)            



def main():
    filesName = "data/full_grades_010a.csv"
    counting_rows(filesName)


if __name__ == "__main__":
    main()