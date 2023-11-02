import csv



def averages(filename):
    min = 100
    max = 0 

    student_grades = []
    with open (filename) as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for line in csv_reader:
            counter = 0
            grade_counter = 0
            
            
            grades = [float(grade) for grade in line[2:10]]
          
            for grade in grades:
            
                counter+=1
                grade_counter+=grade
                grades = grade_counter / counter
                   
            student_grades.append(grades)
            if grades < min:
                min = grades
            if grades > max:
                max = grades
        
        return sum(student_grades) / len(line[2:11]), max, min
      
        
  
            



def main():

    file_name = ("data/grades_010.csv")
    print(averages(file_name))
    #print(sum(averagess) / 8)

if __name__ == "__main__":
    main()