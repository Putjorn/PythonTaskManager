import json
from datetime import datetime

""" data1 = {
    "id":"2",
    "name":"Aof",
    "description":"Design product",
    "due_date":"2026-7-7",
    "isCompleted": False
} """
class Filemanager:
    def loadFile():
        file_path = "data.json"
        try:
            with open(file_path) as file:
                loadData = json.load(file)
                if isinstance(loadData,list):
                    newData = loadData
                    return newData
                else:
                    newData = [loadData]
                    return newData
        except json.JSONDecodeError:
            print(f"Error: File '{file_path}' is not a valid JSON format.")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []


    def saveFile(data):
        with open("data.json","w") as file:
            saveData = json.dump(data, file, indent=4)
            print(f"Already save {saveData}")
    

class Taskmanager:
    def __init__(self):
        self.showData = Filemanager.loadFile()
        

    def addTask(self, name, description, due_date):
        #showData = Filemanager.loadFile()
        #Find len of showData
        task_id = len(self.showData) + 1
        for item in self.showData:                              #If newid = oldid need to change newid
            if item["id"] == task_id:
                lastID = self.showData[len(self.showData) - 1]
                task_id = lastID["id"] + 1

        task_name = name
        description = description
        due_date = due_date
        new_dict = {
            "id": str(task_id),
            "name": task_name,
            "description": description,
            "due_date": due_date,
            "isCompleted": False
        }
        #new_dict append to json file
        self.showData.append(new_dict)
        Filemanager.saveFile(self.showData)


    def showTask(self):
        #self.showData = Filemanager.loadFile()
        print(f"In process task ")
        print("---------------------------------------------------------------------------------------------")
        for item in self.showData:
            if item["isCompleted"] is False:
                print(f"Task_id : {item["id"]} , Task_name : {item["name"]} , Due_date : {item["due_date"]}")
        print("\n" \
        "\n" \
        "---------------------------------------------------------------------------------------------")
        print(f"Completed task ")
        print("---------------------------------------------------------------------------------------------")
        for item in self.showData:
            if item["isCompleted"] is True:
                print(f"Task_id : {item["id"]} , Task_name : {item["name"]} , Due_date : {item["due_date"]}")
        print("\n" \
        "\n" \
        "---------------------------------------------------------------------------------------------")

    def changeStatus(self, id):
        task_id = id
        for item in self.showData:
            if item["id"] == task_id:
                update = item["isCompleted"] = True
                print(update)
        Filemanager.saveFile(self.showData)

    def deleteTask(self, id):
        task_id = id
        for index, item in enumerate(self.showData):
            if item["id"] == task_id:
                print(f"delete_id : {item["id"]} , {self.showData[index]}")
                del self.showData[index]
                print(f"Read all data : {self.showData}")
        Filemanager.saveFile(self.showData)

    def searchTask(self):
        pass

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

def checkDateFormat(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def main():
    app = Taskmanager()
    while True:
        print("Please insert your command")
        print("--------------------------\n"
        "1. Add task\n"
        "2. Show task\n"
        "3. Change status task\n"
        "4. Delete task\n"
        "5. Search task\n"
        "6. Quit programs")
        print("--------------------------\n")
        selected = input("Your command is ")
        print("--------------------------\n")

        if selected == "1":
            print("1. Add task")
            name = input("Name :  ")
            description = input("Description :  ")
            due_date = input("due_date format(YYYY-MM-DD):  ")
            if not name:
                print("Please put name")
            elif not description:
                print("Please put task")
            elif not checkDateFormat(due_date):
                print("Please put follow this format (YYYY-MM-DD)")
            else:
                app.addTask(name, description, due_date)

        elif selected == "2":
            print("2. Show task")
            #showData = Filemanager.loadFile()
            app.showTask()
            #Filemanager.saveFile(data1)
        elif selected == "3":
            print("3. Change status task")
            id = input("task_id : ")
            if not id:
                print("Please insert task_id that you want to change to completed status")
            else:
                app.changeStatus(id)
        elif selected == "4":
            print("4. Delete task")
            id = input("task_id : ")
            if not id:
                print("Please insert task_id that you want to delete")
            else:
                app.deleteTask(id)
        elif selected == "5":
            print("5. Search task")
        elif selected == "6":
            print("6. Quit programs")
            break
        else:
            print("Wrong command please insert again")

if __name__ == "__main__":
    main()
