for i in \'X-token\' \"X-token\"
do
   find . -type f -name "*js*" -exec sed -i '' -e  "s/$i/\/\/$i/g" {} +
   find . -type f -name "*vue*" -exec sed -i '' -e  "s/$i/\/\/$i/g" {} +
done


echo 'be all set, start test'

for l in  replaceStr replaceStr1
do
   grep -r $l ./*  -l
done