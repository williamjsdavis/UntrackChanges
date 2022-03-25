import UntrackChanges as ut
import sys
from os.path import splitext

if __name__ == "__main__":
    filename = str(sys.argv[1])

    with open(filename) as f:
        raw_text = f.read()
    
    b_value = ut.bracket_balance(raw_text)
    
    print('Exited with bracket level:', b_value)
