import unittest

def convert(f, target='c'):    #that's our function that convert fahrenheit to celsius or kelvin  
    if target == 'c':
        return (f - 32) / 1.8
    elif target == 'k':
        return ((f - 32) / 1.8) + 273.15
    else:
        raise Exception('wrong target')

class TestConvert (unittest.TestCase):  #now we proceed testing some result (point 2 and 4)
    def test_division(self):
        self.assertEqual(convert(50,'c'),10)
        self.assertAlmostEqual(convert(70,'c'),21.11111111)
        self.assertAlmostEqual(convert(90,'c'),32.22222222)
        self.assertAlmostEqual(convert(-500,'k'),-22.40555555)
        self.assertAlmostEqual(convert(0,'k'),255.372222)
        self.assertAlmostEqual(convert(1000,'k'),810.9277777)
    def test_wrong_inputs(self):       #here we're texting the else condition, in other words what happen when we give some different information. (point 3)
        with self.assertRaises(Exception):
            convert(70, 'M') 
            

if __name__ == '__main__':
    unittest.main()
