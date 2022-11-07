def exercise1(a, b):
  
  # Lập trình tại đây
  if a>b:
    print("a phải nhỏ hơn b")
  else:
    i=a
    lst = []
    while i in range(a,b+1):
        lst.append(i)
        i+=2
    return convertIS(lst)

def convertIS(lst):
  s = ""
  for i in lst:
    s+= str(i)+" "
  return s.strip()             
            
  
      

# TEST CODE
from unittest import TestCase
import unittest
from unittest.mock import patch
from io import StringIO
try:
    @patch('sys.stdout', new_callable=StringIO)
    def test1(mock_stdout):
        exercise1(10, 1)
        t1 = mock_stdout.getvalue().strip() == "a phải nhỏ hơn b"
        return t1
    
    @patch('sys.stdout', new_callable=StringIO)
    def test2(mock_stdout):
        exercise1(3, 13)
        t2 = mock_stdout.getvalue().strip() == "3 5 7 9 11 13"
        return t2
    
    @patch('sys.stdout', new_callable=StringIO)
    def test3(mock_stdout):
        exercise1(-20, 10)
        t3 = mock_stdout.getvalue().strip() == "-20 -18 -16 -14 -12 -10 -8 -6 -4 -2 0 2 4 6 8 10"
        return t3
    
    @patch('sys.stdout', new_callable=StringIO)
    def test4(mock_stdout):
        exercise1(-9, 30)
        t4 = mock_stdout.getvalue().strip() == "-9 -7 -5 -3 -1 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29"
        return t4
    
    t1 = test1()
    t2 = test2()
    t3 = test3()
    t4 = test4()
    print("Mệnh đề đầu tiên thực hiện đúng?: {}".format(t1))
    print("Mệnh đề thứ hai thực hiện đúng?: {}".format(t2 and t3 and t4))
except Exception as e:
    print("Lỗi thực thi: ", e)
