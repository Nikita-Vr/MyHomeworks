from file_classes import JsonFile, TxtFile, CsvFile

if __name__ == "__main__":
    # Тестирование JsonFile
    print("Testing JsonFile:")
    json_file = JsonFile("data.json")
    json_file.write([{"name": "Alice"}, {"name": "Bob"}])
    print("After write:", json_file.read())
    json_file.append({"name": "Charlie"})
    print("After append:", json_file.read())

    # Тестирование TxtFile
    print("\nTesting TxtFile:")
    txt_file = TxtFile("text.txt")
    txt_file.write("Hello, World!")
    print("After write:", txt_file.read())
    txt_file.append("Additional line")
    print("After append:", txt_file.read())

    # Тестирование CsvFile
    print("\nTesting CsvFile:")
    csv_file = CsvFile("data.csv")
    csv_file.write([["Name", "Age"], ["Alice", "30"], ["Bob", "25"]])
    print("After write:", csv_file.read())
    csv_file.append([["Charlie", "40"], ["David", "35"]])
    print("After append:", csv_file.read())