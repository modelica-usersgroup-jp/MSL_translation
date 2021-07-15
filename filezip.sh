#Remove all *_anno.* files recursively
find * -name "*_anno.*" -type f | sed 's/ /\\ /g' |  xargs rm

zip -R msl_txt "*.txt" 
zip -R msl_pdf "*.pdf" 
zip -R msl_md "*.md" 
zip -R msl_ppt "*.ppt" #Not used
zip -R msl_html "*.html" 
zip -R msl_mo "*.mo" 

#extract html codes in annotation to files named *_anno.html
python3 ../tools/lib_anno.py

#join lines for translating
python3 ../tools/lib_anno_cat.py

#remove the files of size zero
find * -type f -size 0 | sed 's/ /\\ /g' | xargs rm
zip -R msl_anno_html "*_anno.html" 

#change extension from html to txt, because the results of translation are different
find * -type f -name "*_anno.html" | sed 's/ /\\ /g' | xargs rename 's/\.html/.txt/' 
zip -R msl_anno_txt "*_anno.txt" 

find * -name "*_anno.*" -type f | sed 's/ /\\ /g' |  xargs rm
mv msl*.zip ..
