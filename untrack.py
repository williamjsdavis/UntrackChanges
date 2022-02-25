import UntrackChanges as ut
import sys

if __name__ == "__main__":
    filename = str(sys.argv[1])

    with open(filename) as f:
        raw_text = f.read()
    
    new_text = ut.update_text(raw_text)
    new_filename = filename + '.untrack'
    
    with open(new_filename, 'w') as f:
        f.write(new_text)
    print('Success!')
