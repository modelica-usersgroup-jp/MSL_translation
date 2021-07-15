# Make merged library file for MapleSim from descrete library structure

import os # Directry Operation
import re # Regular Expression
import glob # Wildcard

bra = '｟' #skip translation ((
ket = '｠' #skip translation ))

def classload():
  files = os.listdir('.')

  for fn in files:
    #fn = fn.rstrip()
    if os.path.isdir(fn):
      os.chdir(fn)
      print('cd '+fn)
      classload()
      os.chdir('..')
    elif len(fn.split('.')) == 2:
      #if fn.split('.')[1] == 'html':
      if fn.split('.')[1] == 'txt':
        if re.search("_anno", fn):
          print(fn)
          fnmo = fn.split('.')[0].replace('_anno', '')+'.mo'
          print(fnmo)
          annomo = open(fn, 'r')
          annomoltmp = annomo.readlines()
          annomol = []
          for lna in annomoltmp:
            tmp = lna.replace(bra, "\n").replace(ket, "\n")
            tmp = re.sub(' *\. png', '.png', tmp)
            annomol.append(tmp)
          libn = open('tmp', 'w')
          limo = open(fnmo, 'r')
          html_on = 0
          annol = 0
 
          for limol in limo:
            if re.search("<html>", limol):
              html_on = 1
              lna = ''
              while not re.search("</html>", lna):
                lna = annomol.pop(0)
                lna = lna.replace('注釈','\n annotation')
                if re.search("html>", lna):
                  libn.write(lna)
                else:
                  if re.search('\"', re.sub('<[^>]*>','',lna)):
                    if (re.search('img src=', lna) or  re.search('alt=', lna)):
                      libn.write(lna)
                    else:
                      libn.write(lna.replace('\"\"','&quot;').replace('\"','&quot;'))
                  else:
                    libn.write(lna)

            elif re.search("</html>", limol):
              if re.search("<html>", limol):
                libn.write(lna)
                lna = annomol.pop(0)
                while not re.search("</html>", lna):
                  lna = annomol.pop(0)
              else:
                html_on = 0
            else:
              if html_on == 0:
                libn.write(limol)

          libn.close()
          os.rename('tmp', fnmo) 
          limo.close()
          annomo.close()


classload()
 
