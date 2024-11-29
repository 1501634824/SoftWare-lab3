import os

def count_line(folder_path, extensions=None):
    total_line = 0
    for file_name in os.listdir(folder_path):
        if file_name == "count_line.py":
            continue
        file_path = os.path.join(folder_path, file_name)
        if extensions and not any(file_name.endswith(ext) for ext in extensions):
            continue
        with open(file_path, "r", encoding="utf-8") as file:
            file_lines = file.readlines()
            file_count = len(file_lines)
            total_line += file_count
            print(f"文件: {file_name}, 行数: {file_count}")
    return total_line

if __name__ == "__main__":
    total = count_line(".\\", '.py')
    print(f"总行数: {total}")