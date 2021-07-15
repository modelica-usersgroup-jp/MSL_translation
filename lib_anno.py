# Make merged library file for MapleSim from descrete library structure

import os # Directry Operation
import re # Regular Expression

bra = '｟' #skip translation ((
ket = '｠' #skip translation ))

def classload(cn):
  files = os.listdir('.')

  for fn in files:
    fn = fn.rstrip()
    if os.path.isdir(fn):
      os.chdir(fn)
      classload(fn)
      os.chdir('..')
    elif len(fn.split('.')) == 2:
      if fn.split('.')[1] == 'mo':
        print(fn)
        pmo = open(fn, 'r')
        pmoa = open(fn.split('.')[0] + '_anno.html', 'w')
        html_on = 0
        img_flag = 0
        for pmol in pmo:
          if re.search("<html>", pmol):
            html_on = 1
          elif re.search("</html>", pmol):
            html_on = 0
            pmoa.write(bra + pmol.rstrip() + ket + '\n')

          if html_on == 1:
            if re.search("<html>", pmol):
              pmoa.write(bra + pmol.rstrip() + ket + '\n')
            elif re.search("<a href=", pmol):
              pmoa.write(pmol.replace('<', bra+'<').replace('>', '>'+ket) + '\n')
            elif re.search("<img src=", pmol):
              pmol = bra + pmol.rstrip() + ket
              if re.search('<', pmol):
                img_flag = 1
              if img_flag == 1 and re.search('>', pmol):
                img_flag = 0
              pmoa.write(pmol + '\n')
            elif img_flag == 1 and re.search('>', pmol): 
              img_flag = 0
              pmol = bra + pmol.rstrip().replace('>', '>' + ket, 1)
              pmoa.write(pmol + '\n')
            else:
              pmoa.write(pmol)

        pmoa.close()

classload('.')
 
