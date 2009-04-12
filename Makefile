all: c-euler Euler.class fortran-euler

c-euler: euler.c
	# -lgmp -I/opt/local/include -L/opt/local/lib
	gcc -lm -m64 -o c-euler euler.c 

Euler.class: Euler.java
	javac -classpath apfloat.jar Euler.java

run-java: Euler.class
	java -classpath apfloat.jar:. Euler

fortran-euler: euler.for
	gfortran -m64 -fdefault-integer-8 euler.for -o fortran-euler

ScalaEuler.class: ScalaEuler.scala
	/opt/local/scala/bin/scalac -deprecation -classpath apfloat.jar ScalaEuler.scala

run-scala: ScalaEuler.class
	/opt/local/scala/bin/scala -classpath apfloat.jar:. ScalaEuler

clean:
	\rm -f c-euler
