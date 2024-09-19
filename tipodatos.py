print("Clases V2 Angel Valencia")
# zona de clase
class Datos:
    # el constructor funcion
    def __init__(self,estatura,peso):
        self.estatura=estatura
        self.peso=peso
    def mostrar_datos(self):
        print(f"Estatura : {self.estatura}mts, Peso {self.peso} Kg")
    def mi_lista(self):
        futbolistas=["Neymar", "Cr7", "Mbappe"]
        print(futbolistas)
        for fut in futbolistas:
            print(fut)
    def mi_tupla(self):
        tupla_razas=("Doberman","Labrador","Pastor Aleman")
        for b in tupla_razas:
            print(b)

    def mi_conjunto(self):
        conjunto_colores={"morado","azul","negro","amarillo"}
        for c in conjunto_colores:
            print(c)

    def mi_dic(self):
        dic_edadP={"andres":"14","saul":"10","fany":"22"}
        for d,e in dic_edadP.items():
            print(d,e)

# creacion de objeto
info=Datos(1.75,70.5)


# utilizando el obj.--> info
info.mostrar_datos()
print(" Lista de nombres de Futbolistas Angel Valencia")
info.mi_lista()
print("\nTupla razas de perros")
info.mi_tupla()
print("\nConjunto de colores")
info.mi_conjunto()
print("\nDiccionario edades")
info.mi_dic()