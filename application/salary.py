def get_salary_number(salary,month_length,work_days):
    salary_number = round(salary / (month_length * work_days),2)
    salary_amount = f'{int(salary_number * 1000)} руб'
    return print(salary_amount) 
