from application.salary import get_salary_number
from application.db.people import get_employees
from datetime import datetime
from tqdm import tqdm
import time


if __name__ == '__main__':
    get_salary_number(20000,31,21)
    get_employees()
    for i in tqdm(range(1)):
        time.sleep(0.5)
        pass
    print(datetime.today())
    
