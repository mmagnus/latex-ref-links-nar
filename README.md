![sc 2025-04-10 at 16 24 35](https://github.com/user-attachments/assets/f9b023f1-bc40-4a9c-a472-e1b59a79d564)
https://github.com/mmagnus/latex-ref-links-nar/blob/master/demo.pdf

Briefly, the Python script to convert your bib file into NAR required bib format:

Take:

```bibtex
@Article{Magnus22,
  author = {Magnus, M.},
  title = {rna-tools.online: a Swiss army knife for {RNA 3D} structure modeling},
  journal = {NAR},
  year = 2022,
  volume = 50,
  pages = {W657--W662},
  pmid = 35580057,
  pmcid = {PMC9252763},
  doi = {10.1093/nar/gkac372},
}
```
and covert into:
```bibtex
@Article{Magnus22,
  author = {Magnus, M.},
  title = {rna-tools.online: a Swiss army knife for {RNA 3D} structure modeling},
  journal = {NAR},
  year = 2022,
  volume = 50,
  pages = {W657--W662},

  note = {[PubMed:\href{https://www.ncbi.nlm.nih.gov/pubmed/35580057}{35580057}]
          [PubMed Central:\href{https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9252763}{PMC9252763}]
          [doi:\href{https://doi.org/10.1093/nar/gkac372}{10.1093/nar/gkac372}]},

  pmid = 35580057,
  pmcid = {PMC9252763},
  doi = {10.1093/nar/gkac372},
}
```

You can run the demo with the following command:
```shell
    cat test.sh
    python latex-ref-links-nar.py paper.bib paper_nar.bib
    rm *.aux *.bbl *.blg *.log *.out *.toc *.pdf
    file="demo"
    pdflatex ${file}.tex
    bibtex ${file}
    pdflatex ${file}.tex
    pdflatex ${file}.tex
    open ${file}.pdf
```
