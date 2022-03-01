import UntrackChanges as ut
import sys
from os.path import splitext

if __name__ == "__main__":
    filename = str(sys.argv[1])

    with open(filename) as f:
        raw_text = f.read()
    
    new_text = ut.update_text(raw_text)
    
    filename_split = splitext(filename)
    new_filename = filename_split[0] + '-untrack' + filename_split[1]
    
    with open(new_filename, 'w') as f:
        f.write(new_text)
    print('Success!')
