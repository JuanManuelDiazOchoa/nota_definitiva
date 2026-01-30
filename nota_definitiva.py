# Programa para calcular la nota definitiva de una asignatura

#librerias
import math

#-----
#input
#-----

print("                           ")
print("      NOTA DEFINITIVA      ")
print("                           ")

Nc=int(input("digite la nota cognitiva: "))
Np=int(input("digite la nota procediental: "))
Na=int(input("digite la nota actitudinal: "))
Au=int(input("digite la nota autoevauacion: "))
Bi=int(input("digite la nota bimestral: "))

#----------
#Processing
#----------
nd=0.3*Nc+0.3*Np+0.2*Bi+0.1*Na+0.1*Au

#------
#output
#------

print("                      ")
print("      RESULTADOS      ")
print("                      ")
print("La nota definitiva de la asignatura es: " +str(nd))
print("                                                ")