file_path = "D:\\Viswa PYTHON LAB\\sample.txt"
with open(file_path, 'w') as file:
    file.write("Hello Good Morning")
with open(file_path, "r") as file:
    content = file.read()
    print("File content:", content)
