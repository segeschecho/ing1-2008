all: informe.pdf

informe.pdf: glosario.tex informe.tex introduccion.tex requerimientosEspecificos.tex operatoria.tex 
	pdflatex informe.tex  &&  pdflatex informe.tex

clean:
	rm -f *.toc
	rm -f *.aux
	rm -f *.log
	rm -f informe.out
	rm -f informe.pdf
