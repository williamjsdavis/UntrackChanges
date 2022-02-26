import unittest
import os.path

filename = './test/tex-files/short_test1.tex'
new_filename = filename + '.untrack'
reference_filename = filename + '.untrack' + '.reference'

def load_text(filename):
    with open(filename) as f:
        raw_text = f.read()
    return raw_text
def remove_file(new_filename):
    if os.path.isfile(new_filename):
        os.remove(new_filename)
def run_script(filename):
    cmd = 'python untrack.py ' + filename
    os.system(cmd)

class TestSimple(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(1, 1)
        
class TestLoadText(unittest.TestCase):
    def setUp(self):
        self.raw_text = load_text(filename)
    def test_length(self):
        self.assertEqual(len(self.raw_text), 477)
        
class TestFullEdit(unittest.TestCase):
    def setUp(self):
        remove_file(new_filename)
        run_script(filename)
        
        self.raw_text = load_text(filename)
        self.new_text = load_text(new_filename)
        self.reference_text = load_text(reference_filename)
    def tearDown(self):
        remove_file(new_filename)
    def test_change(self):
        if self.raw_text != self.new_text:
            self.assertNotEqual(self.raw_text, self.new_text)
        else:
            self.assertEqual(raw_text, self.new_text)
    def test_output_against_reference(self):
        self.assertEqual(self.new_text, self.reference_text)

if __name__ == '__main__':
    unittest.main()
