import unittest
import os
import sys

sys.path.append("..")
import UntrackChanges.UntrackChanges as ut

filename = './test/tex-files/short-test.tex'
filename_split = os.path.splitext(filename)

new_filename = filename_split[0] + '-untrack' + filename_split[1]
reference_filename = filename_split[0] + '-ref' + filename_split[1]
unbalanced_filename = filename_split[0] + '-unbalanced' + filename_split[1]

def load_text(filename):
    with open(filename) as f:
        raw_text = f.read()
    return raw_text
def remove_file(new_filename):
    if os.path.isfile(new_filename):
        os.remove(new_filename)
def run_script(filename):
    cmd = 'python untrack.py ' + filename + ' >/dev/null 2>&1'
    out = os.system(cmd)
    return out

class TestLoadText(unittest.TestCase):
    def setUp(self):
        self.raw_text = load_text(filename)
    def test_length(self):
        self.assertEqual(len(self.raw_text), 477)
        
class TestBracketBalance(unittest.TestCase):
    def setUp(self):
        self.raw_text = load_text(filename)
        self.raw_unbalancedtext = load_text(unbalanced_filename)
    def test_brackets(self):
        self.assertEqual(ut.bracket_balance(self.raw_text),0)
        self.assertEqual(ut.bracket_balance(self.raw_unbalancedtext),1)

class TestCheckValidity(unittest.TestCase):
    def setUp(self):
        self.raw_text = load_text(filename)
    def test_check_validity(self):
        self.assertTrue(ut.check_validity(self.raw_text))

class TestCheckInvalidity(unittest.TestCase):
    def setUp(self):
        self.raw_text = load_text(unbalanced_filename)
    def test_check_invalidity(self):
        with self.assertRaises(ValueError):
            ut.check_validity(self.raw_text)

class TestFullEditByScript(unittest.TestCase):
    def setUp(self):
        remove_file(new_filename)
        self.outcode = run_script(filename)
        
        self.raw_text = load_text(filename)
        self.new_text = load_text(new_filename)
        self.reference_text = load_text(reference_filename)
    def tearDown(self):
        remove_file(new_filename)
    def test_outcode(self):
        self.assertEqual(self.outcode, 0)
    def test_change(self):
        if self.raw_text != self.new_text:
            self.assertNotEqual(self.raw_text, self.new_text)
        else:
            self.assertEqual(raw_text, self.new_text)
    def test_output_against_reference(self):
        self.assertEqual(self.new_text, self.reference_text)

class TestErrorByScript(unittest.TestCase):
    def setUp(self):
        self.outcode = run_script(unbalanced_filename)
    def test_error_in_brackets_by_script(self):
        self.assertNotEqual(self.outcode, 0)

if __name__ == '__main__':
    unittest.main()
