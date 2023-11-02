import csv



def averages(filename,column):

    
    average_class = 0.0
    AVG_grades = 0
    counter = 0
    with open (filename) as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for line in csv_reader:
            class_average = 0.0
            labs = line[column]
            AVG_grades += float(labs)
            counter+=1
        
          
    average_labs = AVG_grades / counter
        


    return average_labs   
            



def main():

    file_name = ("data/grades_010.csv")
    total_averages = 0.0
    min = 100
    max = 0
    for column in range(2,11):
        average_of_grades = averages(file_name,column)
        

        total_averages += average_of_grades

    
        if average_of_grades < min:
            min = average_of_grades
   
        if average_of_grades > max:
            max = average_of_grades
    print("Maximum",max)
    print("Minimum",min)
    total_Average = total_averages / 9
    print("Average of all classes", total_Average)
    

if __name__ == "__main__":
    main()