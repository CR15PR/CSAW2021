## deda_gui

The objective of this challenge is to find the hidden message in the blank pdf files. The first thing that should come to mind as these are scanned files and the author of the challenge tells us that they were printed, is MIC dots.
A great tool for MIC analysis is [deda](https://pypi.org/project/deda/).

`poppler-utils` is another great resource that can be used for pdf analysis and manipulation. 

`deda_gui` will open a web portal where you can upload files or directories under the forensics tab. 

The pdf must be converted into .png before deda can analyse it.

This can be done with an online converter for through the command line: `dftoppm scan.pdf scan -png`

The output is a pdf file named resultForensic.pdf that has data on the unique mics.

![pic](https://github.com/CR15PR/CSAW2021/blob/main/forensics/mic/mic.png)

The serial of each page (35) can be converted to ascii and we have our flag: `flag{watchoutforthepoisonedcoffee}`

## deda_cli

This is borrowed from https://ctftime.org/writeup/30175 and written by GoProSlowYo but included for others to see how quickly the command line can parce through the images

```pdftoppm scan.pdf scan -png; for x in {01..34}; do echo -n $(python3 -c "print(chr($(deda_parse_print scan-$x.png | grep serial | cut -d '-' -f2 | sed 's/^0*//')))"); done```
