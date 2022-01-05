#!/bin/sh
dot2tex -c -f tikz --prog dot --preproc gp_tree1.dot > tmp.dot
dot2tex -c -f tikz --prog dot -tmath tmp.dot > gp_tree1.tex
pdflatex gp_tree1.tex
dot2tex -c -f tikz --prog dot --preproc gp_tree2.dot > tmp.dot
dot2tex -c -f tikz --prog dot -tmath tmp.dot > gp_tree2.tex
pdflatex gp_tree2.tex
mv gp_tree1.pdf gp_tree2.pdf figures/
