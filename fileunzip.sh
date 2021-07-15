#find * -name "*_anno.html" -type f | sed 's/ /\\ /g' |  xargs rm
#find * -name "*.ja" -type f | xargs rm

unzip ../msl_md_ja.zip
unzip ../msl_mo.zip
unzip ../msl_txt_ja.zip
unzip ../msl_pdf_ja.zip
unzip ../msl_html_ja.zip

#find * -name "*.txt" -type f | sed 's/ /\\ /g' | xargs rename 's/\.txt/_ja.txt/' {}
#find * -name "*.html" -type f | sed 's/ /\\ /g' | xargs rename 's/\.html/_ja.html/' {}

#unzip ../msl_anno_txt_braket_ON_ja.zip
unzip ../msl_anno_txt_braket_ja.zip
python3 ../tools/htmlreturn.py

#find * -name "*anno.html" -type f | sed 's/ /\\ /g' | xargs rm
find * -name "*anno.txt" -type f | sed 's/ /\\ /g' | xargs rm

cd ../MSL_ja
rm -rf *
unzip ../ModelicaStandardLibrary_v4.0.0.zip

cp -a ../work/* .
cp ../README_ja.md .

#find * -name "*anno.txt" -type f | sed 's/ /\\ /g' | xargs rm

zip -r ModelicaStandardLibrary_v4.0.0_ja.zip *
mv *_ja.zip ..

