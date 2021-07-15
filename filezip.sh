#mv ModelicaServices\ 4.0.0/ ModelicaServices4.0.0/
#mv ModelicaReference\ 4.0.0/ ModelicaReference4.0.0/
#mv Modelica\ 4.0.0/ Modelica4.0.0/

find * -name "*_anno.*" -type f | sed 's/ /\\ /g' |  xargs rm

zip -R msl_txt "*.txt" 
zip -R msl_pdf "*.pdf" 
zip -R msl_md "*.md" 
zip -R msl_ppt "*.ppt" 
zip -R msl_html "*.html" 
zip -R msl_mo "*.mo" 

python3 ../tools/lib_anno.py
python3 ../tools/lib_anno_cat.py 

find * -type f -size 0 | sed 's/ /\\ /g' | xargs rm
zip -R msl_anno_html "*_anno.html" 
find * -type f -name "*_anno.html" | sed 's/ /\\ /g' | xargs rename 's/\.html/.txt/' 
zip -R msl_anno_txt "*_anno.txt" 

#mv ModelicaServices4.0.0/ ModelicaServices\ 4.0.0/
#mv ModelicaReference4.0.0/ ModelicaReference\ 4.0.0/
#mv Modelica4.0.0/ Modelica\ 4.0.0/

find * -name "*_anno.*" -type f | sed 's/ /\\ /g' |  xargs rm
mv msl*.zip ..
