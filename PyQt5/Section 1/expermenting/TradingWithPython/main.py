from download import *
from getlink import *
from naming import *
from zipfile import *
import tempfile
import time


# Defining things
global __none

__tempfol = tempfile.gettempdir().replace('\\' , '/')

__desktop_path = str(os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')).replace('\\' , '/')
__none = '$None$'
__output_dir = __desktop_path.__add__('/py-outfile')

def extract(filepath:str , extract_to:str):
    try:
        with ZipFile(filepath, 'r') as zip:
            # Extract all the contents of zip file in current directory
            zip.printdir()
            zip.extractall(extract_to)
            
            print('Done!')
    except FileNotFoundError:
        print('could not download file: skipping...')

def get(date:int, month:int, year:int , output_dir:str=__none, pbar=None) -> None:
    """Will download the file with the given date. and unzip in `output_dir`...\n
    if `output_dir` is not provided, then it will be in `~/desktop/py~outfile`"""
    
    file_link = create_link(date=date , month=month , year=year)
    if output_dir.replace('\\' , '/') !=__none:
        output_folder = output_dir.replace('\\' , '/')
    else:
        tmp = name(file_link).replace('.zip' , '')
        output_folder = __output_dir
        del tmp
    
    file_name = f'{__tempfol}/{name(file_link)}'
    while True:
        i = 0
        try:
            download(url=create_link(date , month , year) , filename=file_name)
            time.sleep(i)
            extract(file_name , output_folder)
            break
        except BadZipfile:
            i += 1
            try:

                os.remove(file_name)
            except:
                pass
            if i > 7:
                print('could not download the file')
                break
            continue
    try:
        os.remove(file_name)
    except:
        pass

def multi_get(from_date:tuple, to_date:tuple):
    pass