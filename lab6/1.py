import os

path_1 = r"C:\Users\Asus\Desktop\pp2\lab6"
for i in os.listdir(path_1):
    path_2 = os.path.join(path_1, i)
    if os.path.isdir(path_2):
        print("Directory:", i)
        for j in os.listdir(path_2):
            path_3 = os.path.join(path_2, j)
            if os.path.isdir(path_3):
                print(f"Directory in {i}:", j)
            elif os.path.isfile(path_3):
                print(f"File in {i}:", j)


    elif os.path.isfile(path_2):
        print("File:", i)