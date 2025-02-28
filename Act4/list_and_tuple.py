students = []

while True:
    print("\nMenu:")
    print("1. Show All Students Record")
    print("2. Order by Last Name")
    print("3. Order by Grade")
    print("4. Show Student Record")
    print("5. Add Record")
    print("6. Edit Record")
    print("7. Delete Record")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nStudent ID  Student Name  Class Standing  Major Exam Grade  Grade")
        print("-" * 60)
        for student in students:
            student_id = student["id"]
            name = student["name"]
            class_standing = student["class_standing"]
            major_exam_grade = student["major_exam_grade"]
            grade = (0.6 * class_standing) + (0.4 * major_exam_grade)
            print(str(student_id) + "  " + name[0] + " " + name[1] + "  " + str(class_standing) + "  " + str(major_exam_grade) + "  " + str(grade))

    elif choice == '2':
        for i in range(len(students)):
            for j in range(i + 1, len(students)):
                if students[i]["name"][1] > students[j]["name"][1]:
                    students[i], students[j] = students[j], students[i]
        print("Students ordered by Last Name:")
        for student in students:
            print(student["name"][0], student["name"][1])

    elif choice == '3':
        for student in students:
            student['grade'] = (0.6 * student["class_standing"]) + (0.4 * student["major_exam_grade"])

        for i in range(len(students)):
            for j in range(i + 1, len(students)):
                if students[i]['grade'] < students[j]['grade']:
                    students[i], students[j] = students[j], students[i]
        print("Students ordered by Grade:")
        for student in students:
            print(student["name"][0], student["name"][1], "- Grade:", (0.6 * student["class_standing"]) + (0.4 * student["major_exam_grade"]))

    elif choice == '4':
        student_id = int(input("Enter Student ID to view: "))
        found = False
        for student in students:
            if student["id"] == student_id:
                print("\nStudent ID:", student['id'])
                print("Name:", student['name'][0], student['name'][1])
                print("Class Standing:", student['class_standing'])
                print("Major Exam Grade:", student['major_exam_grade'])
                grade = (0.6 * student["class_standing"]) + (0.4 * student["major_exam_grade"])
                print("Grade:", grade)
                found = True
                break
        if not found:
            print("Student ID not found!")

    elif choice == '5':
        student_id = int(input("Enter Student ID (6 digits): "))
        if len(str(student_id)) != 6:
            print("Invalid ID! Must be 6 digits.")
            continue
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        name = (first_name, last_name)
        class_standing = float(input("Enter Class Standing: "))
        major_exam_grade = float(input("Enter Major Exam Grade: "))
        students.append({
            "id": student_id,
            "name": name,
            "class_standing": class_standing,
            "major_exam_grade": major_exam_grade
        })
        print("Record added successfully.")

    elif choice == '6':
        student_id = int(input("Enter Student ID to edit: "))
        found = False
        for student in students:
            if student["id"] == student_id:
                print("Editing record for", student['name'][0], student['name'][1])
                first_name = input("Enter First Name (current: " + student['name'][0] + "): ")
                last_name = input("Enter Last Name (current: " + student['name'][1] + "): ")
                name = (first_name, last_name)
                class_standing = float(input("Enter Class Standing (current: " + str(student['class_standing']) + "): "))
                major_exam_grade = float(input("Enter Major Exam Grade (current: " + str(student['major_exam_grade']) + "): "))
                student["name"] = name
                student["class_standing"] = class_standing
                student["major_exam_grade"] = major_exam_grade
                print("Record updated successfully.")
                found = True
                break
        if not found:
            print("Student ID not found!")

    elif choice == '7':
        student_id = int(input("Enter Student ID to delete: "))
        found = False
        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                print("Student record with ID", student_id, "deleted.")
                found = True
                break
        if not found:
            print("Student ID not found!")

    elif choice == '8':
        print("Exiting program.")
        break

    else:
        print("Invalid choice, please try again.")
