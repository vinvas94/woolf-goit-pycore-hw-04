def total_salary(path):
    total=0
    count=0

    try:
        # 1/0
        
        with open (path,"r",encoding="utf-8") as f:
         for line in f:
            try:
                _,salary=line.strip().split(",")
                total+=int(salary)
                count+=1
            except ValueError:
               print (f"Invalid format in the file:{line}")
        # print("Count:", count)       
        if count==0:
            return None
        else:
            average=total/count
            return int(total),int(average)
    except FileNotFoundError:
       print(f"File {path} not found") 
       return None
    except Exception as e:
       print (f"Error {e}")
       return None






total, average = total_salary("task_01/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
