# Complete IEEE journal first draft

Structural Conservatism of Discrete-Time Barrier Certificates:
Moment Obstructions and Degree Separations

Author review draft, October 26, 2026.

## Overleaf

1. Upload TAC_Manuscript_Overleaf.zip as a new project.
2. Set manuscript.tex as the main document.
3. Select pdfLaTeX and compile.

The archive contains manuscript.tex, IEEEtran.cls, geometry.pdf, and this README.
All references are included in manuscript.tex; no BibTeX or external data files are needed.
The official IEEE journal class is used without custom font or page-geometry changes.

## Local build

From the directory containing manuscript.tex:

    latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex

The output is manuscript.pdf (13 pages in the checked build).
No unresolved references or overfull boxes remain. Benign underfull lines can occur in justified IEEE columns.

## Evidence and scope

The paper pins its verification code and exact input data to:
https://github.com/rezairaji60/certificate-expressiveness/tree/7b2d025abdf9786f55819a36b10ffd8a5e343375

From that checkout:

    python src/exact_verify.py
    python src/exact_verify_converse.py
    python src/constructive_converse.py
    python -m unittest discover -s tests -v

All three exact status checks and all 20 tests pass.
The neutral spectral-radius-one converse, automatic body discovery, and optimal component counts remain open.
The authorship order is retained from the supplied VBC/IBC submission for coauthor review.

## Class and figure provenance

IEEEtran.cls is the unmodified official IEEEtran v1.8b class:
https://mirrors.ctan.org/macros/latex/contrib/IEEEtran/IEEEtran.cls
Its copyright, maintenance, and LPPL 1.3 notices remain in the file.

geometry.pdf is the published repository figure, unchanged:
Git blob 03742b7d6f98ad5d3562003483b371d88665682c.
The figure illustrates exact identities; it is not evidence of nonexistence.
