### Extract PDF Pages

<code>pdf_pages_to_png.sh</code> uses the 'convert' command from *ImageMagick* to process pages of a PDF file, converting each specified page into a PNG image.

This script uses a 'for' loop to create PNG files for each specified page in the data/pages directory with the file names **page-019.png**, **page-020.png**, and so on, up to **page-711.png**.


#### Image Conversion:
   - `convert`: This is the ImageMagick tool used to convert files from one format to another.
   - `-background white`: Sets the background color to white.
   - `-flatten`: Merges all layers into one, which is useful when dealing with files with transparency.
   - `-alpha off`: Disables the alpha channel (transparency).
   - `-density 300`: Sets the density (DPI) of the image, which affects the quality of the output. A higher DPI results in a higher-quality image.
   - `-antialias`: Applies an antialiasing filter to smooth out the edges of the image.
   - `-resize 2048x`: Resizes the image to a width of 2048 pixels, maintaining the aspect ratio.
   - `-quality 100`: Sets the quality of the output image. A quality of 100 produces the best image quality.
   - `"input/book.pdf[$i]"`: Specifies the input file and the page number to process.
   - `"data/pages/page-$(printf "%03d" $i).png"`: Specifies the output file path and naming pattern, incorporating the page number variable.
