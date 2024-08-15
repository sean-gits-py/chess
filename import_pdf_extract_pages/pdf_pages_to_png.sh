for i in {19..711}
do
   convert -background white -flatten -alpha off \
    -density 300 -antialias "input/cm_puzzles.pdf[$i]" \
    -resize 2048x -quality 100 "data/pages/page-$(printf "%03d" $i).png"
done
