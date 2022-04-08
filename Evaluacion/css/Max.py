frutas = ["platano","pera","manzana","naranja","kiwi","arandanos"]
precios = [1400,1200,1300,1600,2000,1800]

respuesta = ""
total = 0
while (True):
    print("¿Desea hacer un nuevo pedido de frutas?")
    respuesta = input()
    if(respuesta in ["si","s","SI","Si","sI"]):
        while(True):
            print("¿Qué fruta quiere?")
            respuestaFruta = input()
            aux = respuestaFruta.lower()                     
            if(aux in frutas):
                indexaux = frutas.index("aux")
                print("¿Cuántos kilos?")
                cant = input()
                print("El costo de "+cant+" kilos de "+aux+" cuesta $"+(cant*precios[indexaux]))
                total = cant*precios[indexaux] + total
                respuesta = "seguir"
                break
            else:
                print("La fruta buscada no existe en nuestro inventario")    
    if(respuesta in ["no","n","NO","No","nO"]):
        break
    if(respuesta in ["seguir"]):
        print("\n")
    else:
        print("Debe ingresar 'si' o 'no'")

print("El costo total de su pedido es $"+total)        
