from student import punishmentType, Student, FamilyContact
from utils import clear
import uuid
import json

students = []

def ViewStudents():
  choice = 0
  while True:
    clear()
    print("View students")
    print("---------------")
    print("1. View list of students")
    print("2. View student by name, UUID, DOB")
    print("---------------")
    choice = input("Choice: ")
    try:
      choice = int(choice)
      break
    except:
      print("Try again!")
  if choice == 1:
    clear()
    print("List of students")
    
    currentStudent = 1
    totalStudents = len(students)
    while currentStudent <= totalStudents:
      student = students[currentStudent-1]
      
      name, dob, family = student.getAll()
      uuid = student.getUUID()

      print("--------- Student ---------")
      print(f"Name: {name}")
      print(f"Date of Birth: {dob}")
      print(f"UUID: {str(uuid)}")
      print("--------- Student ---------")

      currentStudent = currentStudent + 1
      input("View next order? ")
    input("")
  elif choice == 2:
    clear()
    print("")
def AddStudent():
  clear()
  while True:
    try:
      name = input("Student name? ").title()
      print("Date of birth")
      day = int(input("Day: "))
      month = int(input("Month: "))
      year = int(input("Year: "))
      dob = str(day)+"/"+str(month)+"/"+str(year)
      studentUUID = str(uuid.uuid4())
      familyMembers = []
      print("\nContact info")
      while True:
        familyMember = input("Family member name: ")
        familyRelation = input("Family relation: ")
        familyPhone = input("Phone number: ")
        familyEmail = input("Email: ")
        familyUUID = str(uuid.uuid4())
        print("----------")
        print(f"Name: {familyMember}")
        print(f"Relation: {familyRelation}")
        print(f"Phone number: {familyPhone}")
        print(f"Email address: {familyEmail}")
        print("----------")
        add = input("Would you like to add this family member? ")
        if add.lower() == "y" or add.lower() == "yes":
          print("Adding...")
          familyMembers.append(FamilyContact(familyUUID, familyMember, familyRelation, familyPhone, familyEmail))
          print("Added!")
        cont = input("Would you like to add another family member? ")
        if cont.lower() == "n" or cont.lower() == "no":
          print("break")
          break
      clear()
      print("--------- Student ---------")
      print(f"Name: {name}")
      print(f"Date of Birth: {dob}")
      print(f"UUID: {str(studentUUID)}")
      print("--------- Family Members ---------")
      for familyMember in familyMembers:
        familyName, familyRelation, familyPhone, familyEmail, familyUUID = familyMember.getAll()
        print(f"---- {familyRelation} ----")
        print(f"Name: {familyName}")
        print(f"Relation: {familyRelation}")
        print(f"Phone: {familyPhone}")
        print(f"Email: {familyEmail}")
        print(f"UUID: {familyUUID}")
      print("----------------")
      add = input("Would you like to add this student? ")
      if add.lower() == "yes" or add.lower() == "y":
        students.append(Student(studentUUID, name, dob, familyMembers))
        print("Added!")
      cont = input("Would you like to add another student? ")
      if cont.lower() == "no" or cont.lower() == "n":
        clear()
        break
    except Exception as e:
      print(e)
      print("Try again")
      continue

def clearStudentsFile():
  global students
  clear()
  print("Clearing students file")
  oldCache = clearStudentCache()
  saveOverwriteStudentsToFile()
  students = oldCache
  clear()

def loadStudentsFromFile():
  clear()
  print("Loading students from file")
  fileName = "students.txt"
  jsonData = None
  with open(fileName) as json_file:
    jsonData = json.load(json_file)
  
  for uuid in jsonData:
    student = jsonData[uuid]
    name, dob, family = student["name"], student["dob"], student["family"]
    familyMembers = []
    for familyUUID in family:
      familyJson = family[familyUUID]
      familyMembers.append(FamilyContact(familyUUID, familyJson["name"], familyJson["relation"], familyJson["phone"], familyJson["email"]))
    students.append(Student(uuid, name, dob, familyMembers))

def clearStudentCache():
  global students
  clear()
  print("Clearing student cache")
  ret = list(students)
  students = []
  return ret

def saveStudentsToFile():
  clear()
  print("Saving students to file")
  fileName = "students.txt"
  jsonData = None
  with open(fileName) as json_file:
    jsonData = json.load(json_file)
  
  for student in students:
    name, dob, family = student.getAll()
    uuid = student.getUUID()
    print(f"Saving: {name}, UUID: {uuid}")
    jsonData[uuid] = {
      "uuid": uuid,
      "name": name,
      "dob": dob,
      "family": family
    }
    print(f"Saved: {name}")
  with open(fileName, 'w') as outfile:
    json.dump(jsonData, outfile)
  print("Saved all :)")
def saveOverwriteStudentsToFile():
  clear()
  print("Saving students to file")
  fileName = "students.txt"
  jsonData = {}
  for student in students:
    name, dob, family = student.getAll()
    uuid = student.getUUID()
    print(f"Saving: {name}, UUID: {uuid}")
    jsonData[uuid] = {
      "uuid": uuid,
      "name": name,
      "dob": dob,
      "family": family
    }
    print(f"Saved: {name}")
  with open(fileName, 'w') as outfile:
    json.dump(jsonData, outfile)
  print("Saved all :)")

menu = {
  "1. View students":ViewStudents,
  "2. Add student":AddStudent,
  "3. Clear students":clearStudentsFile,
  "4. Load students from file":loadStudentsFromFile,
  "6. Clear students cache":clearStudentCache,
  "7. Save students to file":saveStudentsToFile,
  "8. Overwrite save students to file":saveOverwriteStudentsToFile
}
line = "---------- MENU ----------"

while True:
  clear()
  print(line)
  for i in menu: print(i)
  print(line)

  choice = input("")
  try:
    choice = int(choice)
  except:
    print("Try again!")
    continue
  
  for i in menu:
    if str(choice) in i:
      menu[i]()