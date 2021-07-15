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
      classload() #recursive execution
      os.chdir('..')
    elif len(fn.split('.')) == 2:
      #if fn.split('.')[1] == 'html':
      if fn.split('.')[1] == 'txt':
        if re.search("_anno", fn):
          print(fn)
          fnmo = fn.split('.')[0].replace('_anno', '')+'.mo'
          print(fnmo)
          annomo = open(fn, 'r') # translated file
          annomoltmp = annomo.readlines() # read all lines
          annomol = []
          for lna in annomoltmp:
            tmp = lna.replace(bra, "\n").replace(ket, "\n")
            tmp = re.sub(' *\. png', '.png', tmp) # image file name repair 
            annomol.append(tmp) # translated html lines for replace
          libn = open('tmp', 'w')
          limo = open(fnmo, 'r') # original mo file
          html_on = 0
          annol = 0
 
          for limol in limo:
            if re.search("<html>", limol): # html part begin
              html_on = 1
              lna = ''
              while not re.search("</html>", lna):
                lna = annomol.pop(0)
                lna = lna.replace('注釈','\n annotation') # in case
                if re.search("html>", lna):
                  libn.write(lna)
                else:
                  if re.search('\"', re.sub('<[^>]*>','',lna)): # html tag in shortest
                    if (re.search('img src=', lna) or  re.search('alt=', lna)):
                      libn.write(lna)
                    else:
                      libn.write(lna.replace('\"\"','&quot;').replace('\"','&quot;'))
                  else:
                    libn.write(lna)

            elif re.search("</html>", limol):
              if re.search("<html>", limol): # when begin and end in the same line
                libn.write(lna)
                lna = annomol.pop(0)
                while not re.search("</html>", lna): # abandone lines not in html part
                  lna = annomol.pop(0)
              else:
                html_on = 0
            else:
              if html_on == 0: # when program code
                libn.write(limol)

          libn.close()
          os.rename('tmp', fnmo) 
          limo.close()
          annomo.close()


classload()
 
