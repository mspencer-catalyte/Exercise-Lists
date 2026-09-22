
task_list = ["Database Setup", "UI Design", "API Integration", "Security Audit"]

def print_list(array):
    """This function will print all object in input list"""
    print("\r")
    print("Current List:")  
    print(*array, sep = ", ")
    print("\r")     

print_list(task_list)

def change_list(array, position, new_item):
    """This function will put a new item in the place of an older item."""
    true_position = position -1
    array[true_position] = new_item
    print("List updated.")
    print_list(array)

change_list(task_list, 2, "Frontend Framework")

task_list.append("Beta Testing")
print_list(task_list)

task_list.insert(0,"Critical Hotfix")
print_list(task_list)

completed_task = task_list.pop(0)
print("Completed Tasks: ")
print(completed_task)
print_list(task_list)

task_list.remove("Security Audit")
print("List updated.")
print_list(task_list)


task_list = ["Database Setup", "UI Design", "API Integration", "Security Audit"]

task_list.sort(reverse=True)
print("List updated.")
print_list(task_list)


def search_and_destroy(array, target):
    """Performs a safe search-and-destroy operation on an input list"""
    if target in array:
        print("Task found: ")
        print("Removing Task")
        array.remove(target)
        print("List updated.")
        print_list(array)  
    else:
        print("Target not found: ")
        print("List not updated.")
        print_list(array)
        
search_and_destroy(task_list, "API Integrations")

# Modifying a list's length (add / remove) while looping through it 
# in a for loop is not safe. Research why and find a solution. 
"""This is not safe because we could run into an error and crash or skip items in the iteration of the list. """
