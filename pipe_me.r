#!/usr/bin/env Rscript
n <- as.integer(commandArgs(trailingOnly = TRUE)) # Leemos un entero como argumento (opcional)

f <- file("stdin")

open(f)

while(length(line <- readLines(f, n = 1)) > 0) {
   # Aquí habría que hacer cosas más interesantes con la línea
   print(paste0("Linea desde R: " , line))
}

close(f)
