#!/bin/sh
dot2tex -c -f tikz --prog dot --preproc gp_expression_tree1.dot > tmp.dot
dot2tex -c -f tikz --prog dot -tmath tmp.dot > gp_expression_tree1.tex
pdflatex gp_expression_tree1.tex
dot2tex -c -f tikz --prog dot --preproc gp_expression_tree2.dot > tmp.dot
dot2tex -c -f tikz --prog dot -tmath tmp.dot > gp_expression_tree2.tex
pdflatex gp_expression_tree2.tex
dot2tex -c -f tikz --prog dot --preproc gp_derivation_tree1.dot > tmp.dot
dot2tex -c -f tikz --prog dot -tmath tmp.dot > gp_derivation_tree1.tex
pdflatex gp_derivation_tree1.tex
dot2tex -c -f tikz --prog dot --preproc gp_derivation_tree2.dot > tmp.dot
dot2tex -c -f tikz --prog dot -tmath tmp.dot > gp_derivation_tree2.tex
pdflatex gp_derivation_tree2.tex
mv gp_expression_tree1.pdf gp_expression_tree2.pdf gp_derivation_tree1.pdf gp_derivation_tree2.pdf figures/
