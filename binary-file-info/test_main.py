# Write your tests here
from unittest import TestCase
import unittest
from main import file_info

class Test(TestCase):
    def test_no_exist(self):
        pass
    
    def test_pdf(self):
        info = file_info('assets/test01.pdf')
        self.assertEqual(info, 
"""File Statistics:
File Name: assets/test01.pdf
File Size: 33.88 KB
File Type: PDF""")
        
    def test_gif(self):
        pass
    
    def test_png(self):
        pass
    
    def test_jpeg(self):
        pass
    
    def test_deceptive_txt(self):
        pass
    
    def test_deceptive_png(self):
        pass
    
    def test_deceptive_pdf(self):
        pass
    
    def test_deceptive_txt_4(self):
        pass
    
if __name__ == '__main__':
    unittest.main()
