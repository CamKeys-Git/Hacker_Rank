import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
  if s[8:] == 'AM' and s[:2] == '12':
    x = s.replace(s[8:], '')
    x = x.replace(x[0:2], '00')
    return x
  elif s[8:] == 'PM' and s[:2] != '12':
    x = s.replace(s[8:], '')
    i = int(s[:2]) + 12
    x = x.replace(x[0:2], str(i))
    return x
  else:
    x = s.replace(s[8:], '')
    return x 


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
