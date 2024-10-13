from pathlib import Path

with open("salary_file.txt", "r", encoding='utf-8') as fh:
   salary = [el.split(',') for el in fh.readlines()]

                                                                                                # salary = list()
                                                                                                # for line in fh:
                                                                                                #    salary.append(line.split(',')[1])
                                                                                                #    salary = [int(val) for val in salary]

def total_salary(path):
   try:
      total = 0
      for el in salary:
         el[1] = int(el[1])
         total += el[1]
      average = total / len(salary)
      average = int(average)
      salary_tuple = (total, average)
      return salary_tuple
   except Exception as e:
      print(f"{e} with file")

total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

