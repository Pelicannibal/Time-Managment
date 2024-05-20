import sqlite3
from employee import Employee

# Use ':memory:' for testing, the db is wiped after every run
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""") # 3 quotes is a doc string, a string with multiple lines

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
              {'first': emp.first, 'last': emp.last, 'pay': emp.pay})
    
def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                  WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})
        
def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

emp_1 = Employee('John', 'Doe', 8000)
emp_2 = Employee('Jane', 'Doe', 9000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

conn.close()