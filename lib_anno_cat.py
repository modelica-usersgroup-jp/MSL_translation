import os # Directry Operation
import re # Regular Expression

def classload(cn):
  files = os.listdir('.')

  for fn in files:
    fn = fn.rstrip()
    if os.path.isdir(fn):
      os.chdir(fn)
      classload(fn) # recursive execution
      os.chdir('..')
    elif len(fn.split('.')) == 2:
      if re.search('_anno', fn.split('.')[0]): # when *_anno.*
        print(fn)
        pmo = open(fn, 'r')
        pmoa = open('tmp', 'w') # output file
        lncat = ''
        for pmol in pmo:
          if re.search("<html>", pmol): # html part begin
            pmoa.write(pmol)
          elif re.search("</html>", pmol): # html part end
            if lncat != '': # insert \n 
              #lncat = lncat.replace('\. +([A-Z])', ".\n " + m.group(0))
              lncat = lncat.replace('<p>', "\n<p>")
              lncat = lncat.replace('</p>', "</p>\n")
              lncat = lncat.replace('<li>', "\n<li>")
              lncat = lncat.replace('</li>', "</li>\n")
              lncat = lncat.replace('<ol>', "\n<ol>")
              lncat = lncat.replace('</ol>', "</ol>\n")
              lncat = lncat.replace('<ul>', "\n<ul>")
              lncat = lncat.replace('</ul>', "</ul>\n")
              lncat = lncat.replace('<tr>', "\n<tr>")
              lncat = lncat.replace('</tr>', "</tr>\n")
              lncat = lncat.replace('/*', "\n/*")
              lncat = lncat.replace('*/', "*/\n")
              lncat = lncat.replace('<br>', "<br>\n")
              pmoa.write(lncat)
              lncat = ''
            pmoa.write('\n' + pmol)
          else:
            if re.search('//[^Mgw]', pmol): #insert \n in comment line
              lncat = lncat + pmol + '\n'
              #lncat = lncat + pmol.replace('//', '\n//') + '\n'
              #lncat = lncat + '\n' + pmol
            else:
              lncat = lncat + pmol.rstrip() + ' '

        pmoa.close()
        os.rename('tmp', fn)

classload('.')
 
