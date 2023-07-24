# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from Data import DataClass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    d = {
        "id": "1",
        "name": "first",
        "metadata": {
            "system": {
                "size": 10.7
            },
            "user": {
                "batch": 10
            }
        }
    }

    # Converting dict into data class dynamically
    my_inst_1 = DataClass.from_dict(d)
    print("Converting it back to dict from data class", my_inst_1.to_dict())

    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
