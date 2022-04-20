import random

def salary(salary: int, years:int):
    your_skills = []
    year = 1
    new_skills = ['management', 'mentoring', 'postman', 'python', 'sql', 'hacking', 'datascience', 'devops']
    sal = round(salary + salary * (year * 0.4))
    while year != years+1:
        study_skill = random.choice(new_skills)
        exp = round(salary * ((year) * 0.2))
        if study_skill in your_skills:
            print(f'Salary in {year} years - {sal}$. {exp}$ for experience. No bonus')
            sal = round(sal + exp)
        else:
            bonus = random.randint(100, 500)
            print(f'Salary in {year} years - {sal}$. {exp}$ for experience. Bonus for {study_skill} is {bonus}$. Total: {exp+bonus+sal}$')
            your_skills.append(study_skill)
            sal = round((bonus+sal) + exp)
        year += 1

    return your_skills

print('Learned skills:', *salary(400, 7))
