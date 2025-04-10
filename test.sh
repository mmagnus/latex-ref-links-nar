python latex-ref-links-nar.py paper.bib paper_nar.bib
rm *.aux *.bbl *.blg *.log *.out *.toc *.pdf
file="demo"
pdflatex ${file}.tex
bibtex ${file}
pdflatex ${file}.tex
pdflatex ${file}.tex
open ${file}.pdf

#ls Figures/
#pdflatex manuscript.tex
#open manuscript.pdf
#grep '@' paper.bib | wc -l
#biblinker.py paper.bib output.bib
