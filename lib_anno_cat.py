# Make merged library file for MapleSim from descrete library structure

import os # Directry Operation
import re # Regular Expression

def classload(cn):
  files = os.listdir('.')

  for fn in files:
    fn = fn.rstrip()
    if os.path.isdir(fn):
      os.chdir(fn)
      classload(fn)
      os.chdir('..')
    elif len(fn.split('.')) == 2:
      if re.search('_anno', fn.split('.')[0]):
        print(fn)
        pmo = open(fn, 'r')
        pmoa = open('tmp', 'w')
        lncat = ''
        for pmol in pmo:
          if re.search("<html>", pmol):
            pmoa.write(pmol)
          elif re.search("</html>", pmol):
            if lncat != '':
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
            if re.search('//', pmol):
              lncat = lncat + '\n' + pmol
            else:
              lncat = lncat + pmol.rstrip() + ' '

        pmoa.close()
        os.rename('tmp', fn)

classload('.')
 
