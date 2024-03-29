#!/bin/sh
dot2tex -c -f tikz --prog dot --preproc tree_generation_scripts/gp_expression_tree1.dot > tmp.dot
dot2tex -c -f tikz --prog dot -tmath tmp.dot > gp_expression_tree1.tex
pdflatex gp_expression_tree1.tex
dot2tex -c -f tikz --prog dot --preproc tree_generation_scripts/gp_expression_tree2.dot > tmp.dot
dot2tex -c -f tikz --prog dot -tmath tmp.dot > gp_expression_tree2.tex
pdflatex gp_expression_tree2.tex
dot2tex -c -f tikz --prog dot --preproc tree_generation_scripts/gp_derivation_tree1.dot > tmp.dot
dot2tex -c -f tikz --prog dot -tmath tmp.dot > gp_derivation_tree1.tex
pdflatex gp_derivation_tree1.tex
dot2tex -c -f tikz --prog dot --preproc tree_generation_scripts/gp_derivation_tree2.dot > tmp.dot
dot2tex -c -f tikz --prog dot -tmath tmp.dot > gp_derivation_tree2.tex
pdflatex gp_derivation_tree2.tex
dot2tex -c -f tikz --prog dot --preproc tree_generation_scripts/gp_grow_tree.dot > tmp.dot
dot2tex -c -f tikz --prog dot -tmath tmp.dot > gp_grow_tree.tex
pdflatex gp_grow_tree.tex
dot2tex -c -f tikz --prog dot --preproc tree_generation_scripts/gp_grow_tree1.dot > tmp.dot
dot2tex -c -f tikz --prog dot -tmath tmp.dot > gp_grow_tree1.tex
pdflatex gp_grow_tree1.tex
dot2tex -c -f tikz --prog dot --preproc tree_generation_scripts/gp_grow_tree2.dot > tmp.dot
dot2tex -c -f tikz --prog dot -tmath tmp.dot > gp_grow_tree2.tex
pdflatex gp_grow_tree2.tex
mv gp_*.pdf figures/trees/
