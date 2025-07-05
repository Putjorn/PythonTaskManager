import json

""" data = {
    "id":"1",
    "name":"Aof",
    "description":"Design product",
    "due_date":"2026-7-7",
    "isCompleted":False
} """


# Add task // User can add name,descript,due_date => id auto add
# If command add task, declare new dict and json.dump and save in file Json

# Show task // Show all task sperate with isCompleted true/false
# If command show task, read all in Json file and show in command line

# User can change status isCompleted (true) with id task
# If command change status, read file by id and change false to true and save it to Json

# Delete task with id
# If command delete, read file by id and delete it and save to Json

# Save task in JSON file and load when program start
# Start program and read file in Json and keep it in parameter

# Search task by word or date

# CLI
# 1. Add task
# 2. Show task
# 3. Change status
# 4. Delete task
# 5. Search task
# 6. Quit program
### Do not name empty or date
#อย่างน้อย 6 คอมมิตที่มีความหมายซึ่งสะท้อนถึงการเปลี่ยนแปลงหลักในโปรเจกต์ (เช่น การพัฒนาฟังก์ชันหลักของตัวจัดการงาน การเพิ่มฟังก์ชันการทำงานของ JSON การปรับปรุงอินเทอร์เฟซ CLI)

""" with open("data.json","a") as file:
    json.dump(data, file)

with open("data.json") as file:
    print(file.read()) """

def main():
    while True:
        print("Please insert your command")
        print("--------------------------\n"
        "1. Add task\n"
        "2. Show task\n"
        "3. Change status task\n"
        "4. Delete task\n"
        "5. Search task\n"
        "6. Quit programs")
        selected = input("Your command is ")

        if selected == "1":
            print("1. Add task")
        elif selected == "2":
            print("2. Show task")
        elif selected == "3":
            print("3. Change status task")
        elif selected == "4":
            print("4. Delete task")
        elif selected == "5":
            print("5. Search task")
        elif selected == "6":
            print("6. Quit programs")
            break
        else:
            print("Wrong command please insert again")

if __name__ == "__main__":
    main()
