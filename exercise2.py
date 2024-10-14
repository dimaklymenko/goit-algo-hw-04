from pathlib import Path

def get_cats_info(path):
   try:
      with open(path, "r", encoding='utf-8') as fh:
         cats = [el.split(',') for el in fh.readlines()]
      cats_1 = []
      for el in cats:
         el[2] = int(el[2])
         cats_dict = {"id" : el[0], "name" : el[1], "age" : el[2]}
         cats_1.append(cats_dict)  
      return cats_1
   except Exception as e:
      print(f"{e} with file")

cats_info = get_cats_info("cats_file.txt")
print(cats_info)
