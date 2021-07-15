#find * -name "*_anno.html" -type f | sed 's/ /\\ /g' |  xargs rm
#find * -name "*.ja" -type f | xargs rm

# before running this script, download and rename the results of translation as below
# current directory: work
unzip ../msl_md_ja.zip
unzip ../msl_mo.zip
unzip ../msl_txt_ja.zip
unzip ../msl_pdf_ja.zip
unzip ../msl_html_ja.zip

#find * -name "*.txt" -type f | sed 's/ /\\ /g' | xargs rename 's/\.txt/_ja.txt/' {}
#find * -name "*.html" -type f | sed 's/ /\\ /g' | xargs rename 's/\.html/_ja.html/' {}

#unzip ../msl_anno_txt_braket_ON_ja.zip
unzip ../msl_anno_txt_braket_ja.zip
#write the translated text to *.mo files back
python3 ../tools/htmlreturn.py

#find * -name "*anno.html" -type f | sed 's/ /\\ /g' | xargs rm
find * -name "*anno.txt" -type f | sed 's/ /\\ /g' | xargs rm

# working directory: MSL_ja
cd ../MSL_ja
rm -rf *
unzip ../ModelicaStandardLibrary_v4.0.0.zip #Original package

cp -a ../work/* . # copy all translated files
cp ../README_ja.md .

#find * -name "*anno.txt" -type f | sed 's/ /\\ /g' | xargs rm

zip -r ModelicaStandardLibrary_v4.0.0_ja.zip *
mv *_ja.zip ..

