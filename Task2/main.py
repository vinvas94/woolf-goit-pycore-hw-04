def get_cats_info(path):
    cats_info=[]
    try:
        with open (path,"r",encoding="utf-8") as f:
         for line in f:
            cat_id,name,age=line.strip().split(",")
            cat_dict = {"id": cat_id, "name": name, "age": age}
            cats_info.append(cat_dict)
    except FileNotFoundError:
       print(f"File {path} not found") 
    except Exception as e:
       print (f"Error {e}")
    return cats_info
     



cats_info = get_cats_info("Task2/cats_file.txt")
print(cats_info)

# print("{:<30} {:<20} {:<10}".format("CAT_ID", "NAME_CAT", "AGE_CAT"))
# print("-" * 60)

# for cat_info in cats_info:
#     print("{:<30} {:<20} {:<10}".format(cat_info["id"], cat_info["name"], cat_info["age"]))



