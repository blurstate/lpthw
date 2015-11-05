import random

class Score(object):
    def __init__(self, name, gender, score):
        self.student = name
        self.gender = gender.upper()[:1]
        self.score = float(score)
  
def generate_score():
    return random.randint(60,100)   
    
def find_average(scores):
    return round(sum(scores) / len(scores), 1)
    
      
def enter_grades():
    grades = []
    
    grades.append(Score('Joe', 'Male', generate_score()))
    grades.append(Score('Tom', 'male', generate_score()))
    grades.append(Score('Bob', 'M', generate_score()))
    grades.append(Score('Joe', 'm', generate_score()))
    grades.append(Score('Tom', 'M', generate_score()))
    grades.append(Score('Bob', 'M', generate_score()))
    grades.append(Score('Joe', 'M', generate_score()))
    grades.append(Score('Tom', 'M', generate_score()))
    grades.append(Score('Bob', 'M', generate_score()))
    
    grades.append(Score('Sue', 'Female', generate_score()))
    grades.append(Score('Ann', 'female', generate_score()))
    grades.append(Score('Kim', 'F', generate_score()))
    grades.append(Score('Sue', 'f', generate_score()))
    grades.append(Score('Ann', 'F', generate_score()))
    grades.append(Score('Kim', 'F', generate_score()))
    grades.append(Score('Sue', 'F', generate_score()))
    grades.append(Score('Ann', 'F', generate_score()))
    grades.append(Score('Kim', 'F', generate_score()))
    
    return grades
    

def calculate_averages(grades):
    male_grades = []
    female_grades = []
    
    for g in grades:
        if g.gender == 'M':
            male_grades.append(g.score)
        else:
            female_grades.append(g.score)
            
    averages = {
        'male': find_average(male_grades),
        'female': find_average(female_grades),
    }
    
    return averages

def main():
    # add grades
    grades = enter_grades()
    
    # track average scores by gender
    averages = calculate_averages(grades)
    
    print 'Male average', averages['male']
    print 'Female average', averages['female'] 
    
if __name__ == '__main__':
    main()