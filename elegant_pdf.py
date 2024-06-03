import os
import img2pdf
import datetime
from pathlib import Path

while True:
    file_path_str = input("Enter the file or directory path you want to convert or type QUIT to exit >>> ")
    file_path = Path(file_path_str)
    if file_path not in ['quit', 'QUIT']:
        if os.path.isfile(file_path):
            name_stem = os.path.basename(file_path)
            output_filename = f"{name_stem}_{datetime.datetime.now().strftime('%Y%m%_%H%M%S')}.pdf"
            with open(output_filename, mode='wb') as f:
                f.write(img2pdf.convert(file_path))
                print(f"SUCCESS!\t{output_filename} has been saved in the current directory.")
                break
        elif os.path.isdir(file_path):
            list_items = []
            for item in os.listdir(file_path):
                list_items.append(file_path + '//' + item)
            breakpoint()
            # list_items = os.listdir(file_path)
            # for item in list_items:
            #     item = Path.absolute(item)
            # breakpoint()
            desired_extensions = ('.jpg', '.jpeg', '.png')
            items_to_convert = [i for i in list_items if i.endswith(desired_extensions)]
            # name_stem = os.path.basename(file_path)
            # output_filename = f"{name_stem}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            output_filename = "this_is_the_file.pdf"
            image_chunks = img2pdf.convert(items_to_convert)
            # breakpoint()
            with open(output_filename, mode='wb') as f:
                f.write(img2pdf.convert(image_chunks))
                print(f"SUCCESS!\t{output_filename} has been saved in the current directory.")
                break
        else:
            try_again = input(f"{file_path} IS INVALID!")
            continue
    else:
        print("Program was quit.")
        break

print("Program ended elegantly 😃")

'''
THIS IS A .PDF CONVERTER MADE TO CONVERT IMAGES FROM SINGLE FILE OR A DIRECTORY 
TO A .PDF WHICH IS SAVED IN THE CURRENT DIRECTORY.
'''