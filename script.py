# TODO APP in PYTHON

# Modules
import os
import csv


def init_csv(file_name):
    file_path = os.path.join(os.getcwd(), file_name)

    # check if already exists
    if not os.path.exists("file_path"):
        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Tasks", "Status", "Due Date"])


# main() function
def main():
    file_name = "todo.csv"
    init_csv(file_name)


if __name__ == "__main__":
    main()
