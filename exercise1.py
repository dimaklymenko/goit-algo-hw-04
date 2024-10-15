from pathlib import Path
                                                                                        
def total_salary(path):
   try:
      with open(path, "r", encoding='utf-8') as fh:                                       
         some_list = [el.split(',') for el in fh.readlines()]        
      total = 0
      for el in some_list:
         el[1] = float(el[1])
         total += el[1]
      average = total / len(some_list)
      salary_tuple = (total, average)
      return salary_tuple
   except Exception as e:
      print(f"{e} with file")

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


# salary = list()
# for line in fh:
# salary.append(line.split(',')[1])
# salary = [int(val) for val in salary]

