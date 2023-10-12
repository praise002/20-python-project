from unittest import TestCase
import unittest
from main import file_info

class Test(TestCase):
    def test_no_exist(self):
        info = file_info('assets/does-not-exist.txt')
        self.assertEqual(info, "Error: File [assets/does-not-exist.txt] does not exist")

    def test_pdf(self):
        info = file_info('assets/test01.pdf')
        self.assertEqual(info, 
"""File Statistics:
File Name: assets/test01.pdf
File Size: 33.88 KB
File Type: PDF""")

    def test_gif(self):
        info = file_info('assets/test02.gif')
        self.assertEqual(info, 
"""File Statistics:
File Name: assets/test02.gif
File Size: 41.02 KB
File Type: GIF""")

    def test_png(self):
        info = file_info('assets/test03.png')
        self.assertEqual(info, 
"""File Statistics:
File Name: assets/test03.png
File Size: 39.21 KB
File Type: PNG""")

    def test_jpeg(self):
        info = file_info('assets/test04.jpeg')
        self.assertEqual(info, 
"""File Statistics:
File Name: assets/test04.jpeg
File Size: 415.85 KB
File Type: JPEG""")

    def test_txt(self):
        info = file_info('assets/test05.txt')
        self.assertEqual(info, 
"""File Statistics:
File Name: assets/test05.txt
File Size: 13 bytes
File Type: UTF-8 text with BOM""")

    def test_deceptive_txt(self):
        info = file_info('assets/deceptive01.txt')
        self.assertEqual(info, 
"""File Statistics:
File Name: assets/deceptive01.txt
File Size: 10 bytes
File Type: Unknown File Type""")

    def test_deceptive_png(self):
        info = file_info('assets/deceptive02.png')
        self.assertEqual(info, 
"""File Statistics:
File Name: assets/deceptive02.png
File Size: 415.85 KB
File Type: JPEG""")

    def test_deceptive_pdf(self):
        info = file_info('assets/deceptive03.pdf')
        self.assertEqual(info, 
"""File Statistics:
File Name: assets/deceptive03.pdf
File Size: 41.02 KB
File Type: GIF""")

    def test_deceptive_txt_4(self):
        info = file_info('assets/deceptive04.txt')
        self.assertEqual(info, 
"""File Statistics:
File Name: assets/deceptive04.txt
File Size: 39.21 KB
File Type: PNG""")
    
if __name__ == '__main__':
    unittest.main()
