import img2pdf
import datetime
from pathlib import Path
import os

while True:
    single_or_multi = input("This program can convert all images in the current working directory or one image to a "
                            "single .pdf\nType SINGLE or MULTI to choose. Or QUIT to exit >>> ").lower()
    while single_or_multi not in ['quit', 'single', 'multi']:
        print(f"{single_or_multi} IS INVALID!")
        single_or_multi = input("This program can convert all images in the current working directory or one image to "
                                "a single .pdf\nType SINGLE or MULTI to choose. Or QUIT to exit >>> ").lower()
    if single_or_multi == 'single':
        while True:
            input_file = input("Enter the filename of the file to convert >>> ")
            for_stem = Path(input_file)
            if os.path.isfile(input_file):
                name_stem = for_stem.stem
                output_filename = f"{name_stem}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
                with open(output_filename, mode='wb') as f:
                    f.write(img2pdf.convert(input_file))
                    print(f"SUCCESS!\t{output_filename} has been saved in the current directory.")
                    break
            else:
                print(f'{input_file} IS INVALID!')
                input_file = input("Enter the filename of the file to convert >>> ")  # todo could add a quit option
    elif single_or_multi == 'multi':
        current_dir = os.getcwd()
        item_list = os.listdir()
        desired_extensions = ('.jpg', '.jpeg', '.png')
        items_to_convert = [_ for _ in item_list if _.endswith(desired_extensions)]
        output_filename = f"elegant_multi_conversion_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        with open(output_filename, "wb") as f:
            f.write(img2pdf.convert(items_to_convert))
        print("Items were converted successfully")
        break
    else:
        print("Program was quit.")
        break

print("Program ended elegantly 😃")

'''
THIS IS A .PDF CONVERTER MADE TO CONVERT IMAGES FROM A SINGLE FILE OR MULTIPLE FILES 
THE SOURCE FILES NEED TO BE IN THE CURRENT DIRECTORY ALONG WITH THE .PY SCRIPT
THE OUTPUT .PDF WILL BE OUTPUT TO THE SAME CURRENT WORKING DIRECTORY.
'''
