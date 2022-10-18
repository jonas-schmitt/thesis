default: thesis

thesis: main.tex 
	lualatex -shell-escape main.tex
	biber main
	lualatex -shell-escape main.tex
