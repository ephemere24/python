print("CALCULADORA")
print("-----------\n")
#añadir exponente
print("OPCIONES : \n")
print("1. Suma")
print("2. Resta")
print("3. Multiplición")
print("4. División") 
print("5. Descuento sobre precio")
print("6. Raíz cuadrada")
print("7. Exponenciar 'elevar' un número")
print("8. I.V.A")
print("9. Conversor de unidades")


opcion = int(input("\nIntroduce el tipo de operación : "))

while opcion <= 0:
	print("\nOpción no disponible")
	opcion = int(input("\nIntroduce el tipo de operación: "))
while opcion >=10:
	print("\nOpción no disponible")
	opcion = int(input("\nIntroduce el tipo de operación: "))

#SUMA

if opcion == 1:
	print("\nHas seleccionado 'Suma'")
	num_1 = float(input("\nIntroduce el primer valor = "))
	num_2 = float(input("\nIntroduce el segundo valor = "))
	mas = int(input("\nSi deseas añadir mas valores pulsa '0' , de lo contrario pulsa '1'"))
	while mas != 0 and mas !=1:
		print("\nOpción no disponible , intentalo de nuevo :")
		mas = int(input("\nSi deseas añadir mas valores pulsa '0' , de lo contrario pulsa '1'"))
	if mas == 0:
		num_3 = float(input("\nIntroduce el tercer valor = "))
		num_4 = float(input("\nIntroduce el cuarto valor = "))
		resultado = num_1+num_2+num_3+num_4
		print((f"\nResultado : {num_1} + {num_2} + {num_3} + {num_4} = {resultado} "))
	elif mas ==1:
		resultado = num_1+num_2
		print((f"\nResultado : {num_1} + {num_2} = {resultado} "))
	else:
		print("\nOperación no disponible")

		
#RESTA
						
elif opcion == 2:
	print("\nHas seleccionado 'Resta'")
	num_1 = float(input("\nIntroduce el primer valor = "))
	num_2 = float(input("\nIntroduce el segundo valor = "))
	mas = int(input("\nSi deseas añadir mas valores pulsa '0' , de lo contrario pulsa '1'"))
	while mas != 0 and mas !=1:
		print("\nOpción no disponible , intentalo de nuevo :")
		mas = int(input("\nSi deseas añadir mas valores pulsa '0' , de lo contrario pulsa '1'"))
	
	if mas == 0:
		num_3 = float(input("\nIntroduce el tercer valor = "))
		num_4 = float(input("\nIntroduce el cuarto valor = "))
		resultado = num_1-num_2-num_3-num_4
		print((f"\nResultado : {num_1} - {num_2} - {num_3} - {num_4} = {resultado} "))
	elif mas ==1:
		resultado = num_1-num_2
		print((f"\nResultado : {num_1} - {num_2} = {resultado} "))
	else:
		print("\nOperación no disponible")
		
		
#MULTIPLICACIÓN

elif opcion == 3:
	print("\nHas seleccionado 'Multiplicación'")
	num_1 = float(input("\nIntroduce el primer valor = "))
	num_2 = float(input("\nIntroduce el segundo valor = "))
	mas = int(input("\nSi deseas añadir mas valores pulsa '0' , de lo contrario pulsa '1'"))
	while mas != 0 and mas !=1:
		print("\nOpción no disponible , intentalo de nuevo :")
		mas = int(input("\nSi deseas añadir mas valores pulsa '0' , de lo contrario pulsa '1'"))
	
	if mas == 0:
		num_3 = float(input("\nIntroduce el tercer valor = "))
		num_4 = float(input("\nIntroduce el cuarto valor = "))
		resultado = num_1*num_2*num_3*num_4
		print((f"\nResultado : {num_1} x {num_2} x {num_3} x {num_4} = {resultado} "))
	elif mas ==1:
		resultado = num_1*num_2
		print((f"\nResultado : {num_1} x {num_2} = {resultado} "))
	else:
		print("\nOperación no disponible")
		
		
#DIVISIÓN

elif opcion == 4:
	print("\nHas seleccionado 'División'")
	num_1 = float(input("\nIntroduce el primer valor = "))
	num_2 = float(input("\nIntroduce el segundo valor = "))
	mas = int(input("\nSi deseas añadir mas valores pulsa '0' , de lo contrario pulsa '1'"))
	while mas != 0 and mas !=1:
		print("\nOpción no disponible , intentalo de nuevo :")
		mas = int(input("\nSi deseas añadir mas valores pulsa '0' , de lo contrario pulsa '1'"))
		
	if mas == 0:
		num_3 = float(input("\nIntroduce el tercer valor = "))
		num_4 = float(input("\nIntroduce el cuarto valor = "))
		resultado1= num_1/num_2/num_3/num_4
		resultado2= num_1//num_2/num_3//num_4
		resultado3= num_1%num_2%num_3%num_4
			
		print((f"\nResultado : {num_1} / {num_2} / {num_3} / {num_4} = {resultado1:.2f} "))
		print(f"Resultado entero : {resultado2:.2f}")
		print(f"Resultado resto : {resultado3:.2f}")
			
	elif mas ==1:
		resultado = num_1/num_2
		resultado2= num_1//num_2
		resultado3= num_1%num_2
		print(f"\nResultado : {num_1} / {num_2} = {resultado:.2f} ")
		print(f"Resultado entero : {resultado2:.2f}")
		print(f"Resultado resto : {resultado3:.2f}")
	else:
		print("\nOperación no disponible")
		
#DESCUENTO

elif opcion == 5:
	print("\nHas seleccionado 'Descuento sobre precio'")
	num_1 = float(input("\nIntroduce el precio = "))
	num_2 = float(input("\nIntroduce el % de descuento = "))
	
	num_3 = num_2/100
	resultado = num_1*num_3
	total = num_1-resultado
	print(f"\nEl precio con descuento es = {total:.2f}€")
	
#RAIZ CUADRADA	
elif  opcion == 6:
	print("\nHas seleccionado 'Raíz cuadrada'")
	num_1 = float(input("\nIntroduce el numero del que quieres saber su raíz = "))

	while num_1 <=0:
		print("\nEl valor no puede ser igual o inferior a cero")
		num_1 = float(input("\nIntroduce el numero del que quieres saber su raíz = "))
	import math
	resultado = math.sqrt(num_1) 
	
	print(f"\nLa raiz cuadrada de {num_1} es = {resultado:.2f}")
	
#EXPONENTE

elif opcion ==7	:
	print("\nHas seleccionado 'Exponente'")
	numero = float(input("\nIntroduce el numero que deseas elevar : "))
	elevado = int(input("Introduce a que numero quieres elevarlo : "))
	resultado = numero**elevado
	print(f"\nEl resultado de elevar {numero} a {elevado} es = {resultado}")
	
	
#IVA

elif opcion == 8:
	print("\nHas seleccionado I.V.A")
	num_1 = float(input("\nIntroduce el precio : "))
	num_2 = float(input("Introduce el valor del I.V.A 'suele ser 21%' : "))
	
	total = num_1+(num_1*num_2/100)
	print(f"\nEl total del precio con el I.V.A incluido es = {total} ")

	

#CONVERSOR DE UNIDADES
elif opcion == 9 :

	print("\nHas seleccionado Conversor de unidades")
	print("\nOPCIÓNES : ")
	print("\n1. Temperatura --> ( °C,°F,K )")
	print("2. Longitud --> ( km,hm,dam,m,dm,cm,mm )")
	print("3. Masa --> ( Kg,Hg,Dag,g,dg,cg,mg )")
	print("4. Volumen --> kL,hL,daL,L,dl,cl,ml")
	print("5. Velocidad --> ( m/s | km/h )")
	print("6. Tiempo --> ( año,mes,sem,dia,hora,min,seg )")
	print("7. Almacenamiento de datos --> ( Tb,Gb,Mb,Kb,b )")
	print("8. Velocidad+Distancia|Tiempo --> m/s y tiempo en recorrer distancia")
	seleccion= int(input("\nSeleccione un valor : "))

	while seleccion <=0:
		print("\nOpción no disponible , intentelo de nuevo.")
		seleccion= int(input("\nSeleccione un valor : "))

	while seleccion >=9:
		print("\nOpción no disponible , intentelo de nuevo.")
		seleccion= int(input("\nSeleccione un valor : "))


#TEMPERATURA
	
	if seleccion == 1:
		print("\nHas seleccionado 'Temperatura'")
		
		print("\n1. °C a °F")
		print("2. °C a K")
		print("3. °F a °C")
		print("4. °F a K")
		print("5. K a °C")
		print("6. K a °F")
		
		opcion_1 = int(input("\nSeleccione una medida a convertir : "))
		
		while opcion_1 <= 0:
			print("\nOpcion no valida , intentalo de nuevo ")
			opcion_1 = int(input("\nSeleccione una medida a convertir : "))
		while opcion_1 >= 7 :
			print("\nOpcion no valida , intentalo de nuevo ")
			opcion_1 = int(input("\nSeleccione una medida a convertir : "))

#c f	
		if opcion_1 == 1:
			print("\nHas seleccionado : °C/°F")
			grados = int(input("\nIntroduce los grados : "))
			grados = (grados*9/5)+32
			print(f"\nEl resultado es {grados:.2f} grados Fahrenheit")
			
#c k			
		elif opcion_1 == 2:
			print("\nHas seleccionado : °C/K")
			grados = int(input("\nIntroduce los grados : "))
			grados = (grados+273.15)
			print(f"\nEl resultado es {grados:.2f} grados Kelvin")
			
#f c		
		elif opcion_1 == 3:
			print("\nHas seleccionado : °F/°C")
			grados = int(input("\nIntroduce los grados : "))
			grados = (grados-32)*5/9
			print(f"\nEl resultado es {grados:.2f} grados Celsius")

#f k						
		elif opcion_1 == 4:
			print("\nHas seleccionado : °F/K")
			grados = int(input("\nIntroduce los grados : "))
			grados = (grados-32)*5/9+273.15
			print(f"\nEl resultado es {grados:.2f} grados Kelvin")
#k c			
		elif opcion_1 == 5:
			print("\nHas seleccionado : K/°C")
			grados = int(input("\nIntroduce los grados : "))
			grados = (grados-273.15)
			print(f"\nEl resultado es {grados:.2f} grados Celsius")

#k f		
		elif opcion_1 == 6:
			print("\nHas seleccionado : K/°F")
			grados = int(input("\nIntroduce los grados : "))
			grados = (grados-273.15)*9/5+32
			print(f"\nEl resultado es {grados:.2f} grados Fahrenheit")
			


#LONGITUD ( km,hm,dam,m,dm,cm,mm ) CAMBIAR A ELIF!!!

	elif seleccion ==2:
		print("\nHas seleccionado 'Longitud'")
			
		print("\n1. Km")
		print("2. Hm")
		print("3. Dam")
		print("4. M")
		print("5. dm")
		print("6. cm")
		print("7. mm")
			
		longitud = int(input("\nSeleccione la medida de origen : "))
			
		longitud_2 = int(input("\nSeleccione la medida de salida : "))

		while longitud <= 0 or  longitud >= 8:
			print("\nOpción no disponible , intentalo de nuevo")
			opcion = int(input("\nIntroduce el tipo de operación: "))
		while longitud_2 <=0 or longitud_2 >= 8:
			print("\nOpción no disponible , intentalo de nuevo")
			opcion = int(input("\nIntroduce el tipo de operación: "))


#km a...
	#km a km			
		if longitud == 1 and longitud_2 == 1:
			cuanto = float(input("\nInserte los Km que desea convertir a Km :	"))
				
			total = cuanto*1
			print(f"\nEl resultado es {total}Km")
	#km a hm
		if longitud ==1 and longitud_2==2:
			cuanto = float(input("\nInserte los Km que desea convertir a Hm :	"))
			total = (cuanto*10)
			print(f"\nEl resultado es {total}Hm")
			
	#km a dam
		if longitud ==1 and longitud_2==3:
			cuanto = float(input("\nInserte los Km que desea convertir a Dam :	"))
			total = (cuanto*100)
			print(f"\nEl resultado es {total}Dam")
			
	#km a m
		if longitud ==1 and longitud_2==4:
			cuanto = float(input("\nInserte los Km que desea convertir a M :	"))
			total = (cuanto*1000)
			print(f"\nEl resultado es {total}M")
			
	#km a dm
		if longitud ==1 and longitud_2==5:
			cuanto = float(input("\nInserte los Km que desea convertir a dm :	"))
			total = (cuanto*10000)
			print(f"\nEl resultado es {total}dm")
			
			
	#km a cm
		if longitud ==1 and longitud_2==6:
			cuanto = float(input("\nInserte los Km que desea convertir a cm :	"))
			total = (cuanto*100000)
			print(f"\nEl resultado es {total}cm")
			
			
	#km a mm
		if longitud ==1 and longitud_2==7:
			cuanto = float(input("\nInserte los Km que desea convertir a mm :	"))
			total = (cuanto*1000000)
			print(f"\nEl resultado es {total}mm")

	
		
			
#Hm a...

	#Hm a km			
		if longitud == 2 and longitud_2 == 1:
			cuanto = float(input("\nInserte los Hm que desea convertir a Km :	"))
					
			total = cuanto/10
			print(f"\nEl resultado es {total}Km")
	#Hm a hm
		if longitud ==2 and longitud_2==2:
			cuanto = float(input("\nInserte los Hm que desea convertir a Hm :	"))
			total = (cuanto*1)
			print(f"\nEl resultado es {total}Hm")
				
	#Hm a dam
		if longitud ==2 and longitud_2==3:
			cuanto = float(input("\nInserte los Hm que desea convertir a Dam :	"))
			total = (cuanto*10)
			print(f"\nEl resultado es {total}Dam")
				
	#Hm a m
		if longitud ==2 and longitud_2==4:
			cuanto = float(input("\nInserte los Hm que desea convertir a M :	"))
			total = (cuanto*100)
			print(f"\nEl resultado es {total}M")
				
	#Hm a dm
		if longitud ==2 and longitud_2==5:
			cuanto = float(input("\nInserte los Hm que desea convertir a dm :	"))
			total = (cuanto*1000)
			print(f"\nEl resultado es {total}dm")
				
				
	#Hm a cm
		if longitud ==2 and longitud_2==6:
			cuanto = float(input("\nInserte los Hm que desea convertir a cm :	"))
			total = (cuanto*10000)
			print(f"\nEl resultado es {total}cm")
				
				
	#Hm a mm
		if longitud ==2 and longitud_2==7:
			cuanto = float(input("\nInserte los Hm que desea convertir a mm :	"))
			total = (cuanto*100000)
			print(f"\nEl resultado es {total}mm")
			
						
#dam a...

	#dam a km			
		if longitud == 3 and longitud_2 == 1:
			cuanto = float(input("\nInserte los Dam que desea convertir a Km :	"))
					
			total = cuanto/100
			print(f"\nEl resultado es {total}Km")
	#dam a hm
		if longitud ==3 and longitud_2==2:
			cuanto = float(input("\nInserte los Dam que desea convertir a Hm :	"))
			total = (cuanto/10)
			print(f"\nEl resultado es {total}Hm")
				
	#dam a dam
		if longitud ==3 and longitud_2==3:
			cuanto = float(input("\nInserte los Dam que desea convertir a Dam :	"))
			total = (cuanto*1)
			print(f"\nEl resultado es {total}Dam")
				
	#dam a m
		if longitud ==3 and longitud_2==4:
			cuanto = float(input("\nInserte los Dam que desea convertir a M :	"))
			total = (cuanto*10)
			print(f"\nEl resultado es {total}M")
				
	#dam a dm
		if longitud ==3 and longitud_2==5:
			cuanto = float(input("\nInserte los Dam que desea convertir a dm :	"))
			total = (cuanto*100)
			print(f"\nEl resultado es {total}dm")
				
				
	#dam a cm
		if longitud ==3 and longitud_2==6:
			cuanto = float(input("\nInserte los Dam que desea convertir a cm :	"))
			total = (cuanto*1000)
			print(f"\nEl resultado es {total}cm")
				
				
	#dam a mm
		if longitud ==3 and longitud_2==7:
			cuanto = float(input("\nInserte los Dam que desea convertir a mm :	"))
			total = (cuanto*10000)
			print(f"\nEl resultado es {total}mm")
			
			
			
# ( km,hm,dam,m,dm,cm,mm )



#m a...

	#m a km			
		if longitud == 4 and longitud_2 == 1:
			cuanto = float(input("\nInserte los M que desea convertir a Km :	"))
					
			total = cuanto/1000
			print(f"\nEl resultado es {total}Km")
	#m a hm
		if longitud ==4 and longitud_2==2:
			cuanto = float(input("\nInserte los M que desea convertir a Hm :	"))
			total = (cuanto/100)
			print(f"\nEl resultado es {total}Hm")
				
	#m a dam
		if longitud ==4 and longitud_2==3:
			cuanto = float(input("\nInserte los M que desea convertir a Dam :	"))
			total = (cuanto/10)
			print(f"\nEl resultado es {total}Dam")
				
	#m a m
		if longitud ==4 and longitud_2==4:
			cuanto = float(input("\nInserte los M que desea convertir a M :	"))
			total = (cuanto*1)
			print(f"\nEl resultado es {total}M")
				
	#m a dm
		if longitud ==4 and longitud_2==5:
			cuanto = float(input("\nInserte los M que desea convertir a dm :	"))
			total = (cuanto*10)
			print(f"\nEl resultado es {total}dm")
				
				
	#m a cm
		if longitud ==4 and longitud_2==6:
			cuanto = float(input("\nInserte los M que desea convertir a cm :	"))
			total = (cuanto*100)
			print(f"\nEl resultado es {total}cm")
				
				
	#m a mm
		if longitud ==4 and longitud_2==7:
			cuanto = float(input("\nInserte los M que desea convertir a mm :	"))
			total = (cuanto*1000)
			print(f"\nEl resultado es {total}mm")
			


#dm a...

	#dm a km			
		if longitud == 5 and longitud_2 == 1:
			cuanto = float(input("\nInserte los dm que desea convertir a Km :	"))
					
			total = cuanto/10000
			print(f"\nEl resultado es {total}Km")
	#dm a hm
		if longitud ==5 and longitud_2==2:
			cuanto = float(input("\nInserte los dm que desea convertir a Hm :	"))
			total = (cuanto/1000)
			print(f"\nEl resultado es {total}Hm")
				
	#dm a dam
		if longitud ==5 and longitud_2==3:
			cuanto = float(input("\nInserte los dm que desea convertir a Dam :	"))
			total = (cuanto/100)
			print(f"\nEl resultado es {total}Dam")
				
	#dm a m
		if longitud ==5 and longitud_2==4:
			cuanto = float(input("\nInserte los dm que desea convertir a M :	"))
			total = (cuanto/10)
			print(f"\nEl resultado es {total}M")
				
	#dm a dm
		if longitud ==5 and longitud_2==5:
			cuanto = float(input("\nInserte los dm que desea convertir a dm :	"))
			total = (cuanto*1)
			print(f"\nEl resultado es {total}dm")
				
				
	#dm a cm
		if longitud ==5 and longitud_2==6:
			cuanto = float(input("\nInserte los dm que desea convertir a cm :	"))
			total = (cuanto*10)
			print(f"\nEl resultado es {total}cm")
				
				
	#dm a mm
		if longitud ==5 and longitud_2==7:
			cuanto = float(input("\nInserte los dm que desea convertir a mm :	"))
			total = (cuanto*100)
			print(f"\nEl resultado es {total}mm")
			
			


#cm a...

	#cm a km			
		if longitud == 6 and longitud_2 == 1:
			cuanto = float(input("\nInserte los cm que desea convertir a Km :	"))
					
			total = cuanto/100000
			print(f"\nEl resultado es {total}Km")
	#cm a hm
		if longitud ==6 and longitud_2==2:
			cuanto = float(input("\nInserte los cm que desea convertir a Hm :	"))
			total = (cuanto/10000)
			print(f"\nEl resultado es {total}Hm")
				
	#cm a dam
		if longitud ==6 and longitud_2==3:
			cuanto = float(input("\nInserte los cm que desea convertir a Dam :	"))
			total = (cuanto/1000)
			print(f"\nEl resultado es {total}Dam")
				
	#cm a m
		if longitud ==6 and longitud_2==4:
			cuanto = float(input("\nInserte los cm que desea convertir a M :	"))
			total = (cuanto/100)
			print(f"\nEl resultado es {total}M")
				
	#cm a dm
		if longitud ==6 and longitud_2==5:
			cuanto = float(input("\nInserte los cm que desea convertir a dm :	"))
			total = (cuanto/10)
			print(f"\nEl resultado es {total}dm")
				
				
	#cm a cm
		if longitud ==6 and longitud_2==6:
			cuanto = float(input("\nInserte los cm que desea convertir a cm :	"))
			total = (cuanto*1)
			print(f"\nEl resultado es {total}cm")
				
				
	#cm a mm
		if longitud ==6 and longitud_2==7:
			cuanto = float(input("\nInserte los cm que desea convertir a mm :	"))
			total = (cuanto*10)
			print(f"\nEl resultado es {total}mm")
			
			
			
			
#mm a...

	#mm a km			
		if longitud == 7 and longitud_2 == 1:
			cuanto = float(input("\nInserte los mm que desea convertir a Km :	"))
					
			total = cuanto/1000000
			print(f"\nEl resultado es {total}Km")
	#mm a hm
		if longitud ==7 and longitud_2==2:
			cuanto = float(input("\nInserte los mm que desea convertir a Hm :	"))
			total = (cuanto/100000)
			print(f"\nEl resultado es {total}Hm")
				
	#mm a dam
		if longitud ==7 and longitud_2==3:
			cuanto = float(input("\nInserte los mm que desea convertir a Dam :	"))
			total = (cuanto/10000)
			print(f"\nEl resultado es {total}Dam")
				
	#mm a m
		if longitud ==7 and longitud_2==4:
			cuanto = float(input("\nInserte los mm que desea convertir a M :	"))
			total = (cuanto/1000)
			print(f"\nEl resultado es {total}M")
				
	#mm a dm
		if longitud ==7 and longitud_2==5:
			cuanto = float(input("\nInserte los mm que desea convertir a dm :	"))
			total = (cuanto/100)
			print(f"\nEl resultado es {total}dm")
				
				
	#mm a cm
		if longitud ==7 and longitud_2==6:
			cuanto = float(input("\nInserte los mm que desea convertir a cm :	"))
			total = (cuanto*10)
			print(f"\nEl resultado es {total}cm")
				
				
	#mm a mm
		if longitud ==7 and longitud_2==7:
			cuanto = float(input("\nInserte los mm que desea convertir a mm :	"))
			total = (cuanto*1)
			print(f"\nEl resultado es {total}mm")
			
			

#MASA Kg,Hg,Dag,g,dg,cg,mg


	elif seleccion == 3:
		
		print("\nHas seleccionado 'Masa'")
		
		print("\n1. Kg")
		print("2. Hg")
		print("3. Dag")
		print("4. g")
		print("5. dg")
		print("6. cg")
		print("7. mg")
		
		valor_1 = int(input("\nIntroduce la unidad que quieres convertir : "))
		
		while valor_1 <=0 or valor_1 >= 8:
			print("\nOpción no disponible , intentelo de nuevo")
			valor_1 = int(input("\nIntroduce la unidad que quieres convertir : "))
	
		valor_2 = int(input("\nIntroduce la unidad a la que quiere convertir : "))

		while valor_2 <=0 or valor_2 >= 8:
			print("\nOpción no disponible , intentelo de nuevo")
			valor_2 = int(input("\nIntroduce la unidad que quieres convertir : "))
#1kg a..
	#kg a kg
		if valor_1 ==1 and valor_2 == 1:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1
			print(f"\nEl resultado es = {total}Kg")
	
	#kg a hg
		elif valor_1 ==1 and valor_2 == 2:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10
			print(f"\nEl resultado es = {total}Hg")			

	#kg a Dag
		elif valor_1 ==1 and valor_2 == 3:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*100
			print(f"\nEl resultado es = {total}Dag")			
			
			
	#kg a g
		elif valor_1 ==1 and valor_2 == 4:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1000
			print(f"\nEl resultado es = {total}g")
			
	#kg a dg
		elif valor_1 ==1 and valor_2 == 5:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10000
			print(f"\nEl resultado es = {total}dg")
						
	#kg a cg
		elif valor_1 ==1 and valor_2 == 6:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*100000
			print(f"\nEl resultado es = {total}cg")
			
	#kg a mg
		elif valor_1 ==1 and valor_2 == 7:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1000000
			print(f"\nEl resultado es = {total}mg")
			
                                                                           			
			
#2Hg a..
	#Hg a kg
		elif valor_1 ==2 and valor_2 == 1:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10
			print(f"\nEl resultado es = {total}Kg")
	
	#Hg a hg
		elif valor_1 ==2 and valor_2 == 2:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1
			print(f"\nEl resultado es = {total}Hg")			

	#Hg a Dag
		elif valor_1 ==2 and valor_2 == 3:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10
			print(f"\nEl resultado es = {total}Dag")			
			
			
	#Hg a g
		elif valor_1 ==2 and valor_2 == 4:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*100
			print(f"\nEl resultado es = {total}g")
			
	#Hg a dg
		elif valor_1 ==2 and valor_2 == 5:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1000
			print(f"\nEl resultado es = {total}dg")
						
	#Hg a cg
		elif valor_1 ==2 and valor_2 == 6:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10000
			print(f"\nEl resultado es = {total}cg")
			
	#Hg a mg
		elif valor_1 ==2 and valor_2 == 7:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*100000
			print(f"\nEl resultado es = {total}mg")
			
			
			
                                                                           			
			
#3Dag a..
	#Dag a kg
		elif valor_1 ==3 and valor_2 == 1:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/100
			print(f"\nEl resultado es = {total}Kg")
	
	#Dag a hg
		elif valor_1 ==3 and valor_2 == 2:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10
			print(f"\nEl resultado es = {total}Hg")			

	#Dag a Dag
		elif valor_1 ==3 and valor_2 == 3:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1
			print(f"\nEl resultado es = {total}Dag")			
			
			
	#Dag a g
		elif valor_1 ==3 and valor_2 == 4:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10
			print(f"\nEl resultado es = {total}g")
			
	#Dag a dg
		elif valor_1 ==3 and valor_2 == 5:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*100
			print(f"\nEl resultado es = {total}dg")
						
	#Dag a cg
		elif valor_1 ==3 and valor_2 == 6:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1000
			print(f"\nEl resultado es = {total}cg")
			
	#Dag a mg
		elif valor_1 ==3 and valor_2 == 7:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10000
			print(f"\nEl resultado es = {total}mg")
			
	
			
                                                                           			
			
#4g a..
	#g a kg
		elif valor_1 ==4 and valor_2 == 1:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/1000
			print(f"\nEl resultado es = {total}Kg")
	
	#g a hg
		elif valor_1 ==4 and valor_2 == 2:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/100
			print(f"\nEl resultado es = {total}Hg")			

	#g a Dag
		elif valor_1 ==4 and valor_2 == 3:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10
			print(f"\nEl resultado es = {total}Dag")			
			
			
	#g a g
		elif valor_1 ==4 and valor_2 == 4:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1
			print(f"\nEl resultado es = {total}g")
			
	#g a dg
		elif valor_1 ==4 and valor_2 == 5:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10
			print(f"\nEl resultado es = {total}dg")
						
	#g a cg
		elif valor_1 ==4 and valor_2 == 6:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*100
			print(f"\nEl resultado es = {total}cg")
			
	#g a mg
		elif valor_1 ==4 and valor_2 == 7:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1000
			print(f"\nEl resultado es = {total}mg")
			
			

                                                                           			
			
#5dg a..
	#dg a kg
		elif valor_1 ==5 and valor_2 == 1:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10000
			print(f"\nEl resultado es = {total}Kg")
	
	#dg a hg
		elif valor_1 ==5 and valor_2 == 2:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/1000
			print(f"\nEl resultado es = {total}Hg")			

	#dg a Dag
		elif valor_1 ==5 and valor_2 == 3:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/100
			print(f"\nEl resultado es = {total}Dag")			
			
			
	#dg a g
		elif valor_1 ==5 and valor_2 == 4:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10
			print(f"\nEl resultado es = {total}g")
			
	#dg a dg
		elif valor_1 ==5 and valor_2 == 5:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1
			print(f"\nEl resultado es = {total}dg")
						
	#dg a cg
		elif valor_1 ==5 and valor_2 == 6:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10
			print(f"\nEl resultado es = {total}cg")
			
	#dg a mg
		elif valor_1 ==5 and valor_2 == 7:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*100
			print(f"\nEl resultado es = {total}mg")
			
			
			
                                                                           			
			
#6cg a..
	#cg a kg
		elif valor_1 ==6 and valor_2 == 1:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/100000
			print(f"\nEl resultado es = {total}Kg")
	
	#cg a hg
		elif valor_1 ==6 and valor_2 == 2:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10000
			print(f"\nEl resultado es = {total}Hg")			

	#cg a Dag
		elif valor_1 ==6 and valor_2 == 3:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/1000
			print(f"\nEl resultado es = {total}Dag")			
			
			
	#cg a g
		elif valor_1 ==6 and valor_2 == 4:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/100
			print(f"\nEl resultado es = {total}g")
			
	#cg a dg
		elif valor_1 ==6 and valor_2 == 5:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10
			print(f"\nEl resultado es = {total}dg")
						
	#cg a cg
		elif valor_1 ==6 and valor_2 == 6:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1
			print(f"\nEl resultado es = {total}cg")
			
	#cg a mg
		elif valor_1 ==6 and valor_2 == 7:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10
			print(f"\nEl resultado es = {total}mg")
			
			
			
                                                                           			
			
#7mg a..
	#mg a kg
		elif valor_1 ==7 and valor_2 == 1:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/1000000
			print(f"\nEl resultado es = {total}Kg")
	
	#mg a hg
		elif valor_1 ==7 and valor_2 == 2:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/100000
			print(f"\nEl resultado es = {total}Hg")			

	#mg a Dag
		elif valor_1 ==7 and valor_2 == 3:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10000
			print(f"\nEl resultado es = {total}Dag")			
			
			
	#mg a g
		elif valor_1 ==7 and valor_2 == 4:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/1000
			print(f"\nEl resultado es = {total}g")
			
	#mg a dg
		elif valor_1 ==7 and valor_2 == 5:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/100
			print(f"\nEl resultado es = {total}dg")
						
	#mg a cg
		elif valor_1 ==7 and valor_2 == 6:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10
			print(f"\nEl resultado es = {total}cg")
			
	#mg a mg
		elif valor_1 ==7 and valor_2 == 7:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1
			print(f"\nEl resultado es = {total}mg")
			





#Volumen		
		
		
		
	elif seleccion == 4:
		
		print("\nHas seleccionado 'Volumen'")
		
		print("\n1. Kl")
		print("2. Hl")
		print("3. Dal")
		print("4. l")
		print("5. dl")
		print("6. cl")
		print("7. ml")
		
		valor_1 = int(input("\nIntroduce la unidad que quieres convertir : "))
		
		while valor_1 <=0 or valor_1 >= 8:
			print("\nOpción no disponible , intentelo de nuevo")
			valor_1 = int(input("\nIntroduce la unidad que quieres convertir : "))
	
		valor_2 = int(input("\nIntroduce la unidad a la que quiere convertir : "))

		while valor_2 <=0 or valor_2 >= 8:
			print("\nOpción no disponible , intentelo de nuevo")
			valor_2 = int(input("\nIntroduce la unidad que quieres convertir : "))
#kl a..
	#kl a kl
		if valor_1 ==1 and valor_2 == 1:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1
			print(f"\nEl resultado es = {total}Kl")
	
	#kl a hl
		elif valor_1 ==1 and valor_2 == 2:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10
			print(f"\nEl resultado es = {total}Hl")			

	#kl a Dal
		elif valor_1 ==1 and valor_2 == 3:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*100
			print(f"\nEl resultado es = {total}Dal")			
			
			
	#kl a l
		elif valor_1 ==1 and valor_2 == 4:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1000
			print(f"\nEl resultado es = {total}l")
			
	#kl a dl
		elif valor_1 ==1 and valor_2 == 5:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10000
			print(f"\nEl resultado es = {total}dl")
						
	#kl a cl
		elif valor_1 ==1 and valor_2 == 6:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*100000
			print(f"\nEl resultado es = {total}cl")
			
	#kl a ml
		elif valor_1 ==1 and valor_2 == 7:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1000000
			print(f"\nEl resultado es = {total}ml")
			
                                                                           			
			
#Hl a..
	#Hl a kl
		elif valor_1 ==2 and valor_2 == 1:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10
			print(f"\nEl resultado es = {total}Kl")
	
	#Hl a hl
		elif valor_1 ==2 and valor_2 == 2:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1
			print(f"\nEl resultado es = {total}Hl")			

	#Hl a Dal
		elif valor_1 ==2 and valor_2 == 3:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10
			print(f"\nEl resultado es = {total}Dal")			
			
			
	#Hl a l
		elif valor_1 ==2 and valor_2 == 4:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*100
			print(f"\nEl resultado es = {total}l")
			
	#Hl a dl
		elif valor_1 ==2 and valor_2 == 5:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1000
			print(f"\nEl resultado es = {total}dl")
						
	#Hl a cl
		elif valor_1 ==2 and valor_2 == 6:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10000
			print(f"\nEl resultado es = {total}cl")
			
	#Hl a ml
		elif valor_1 ==2 and valor_2 == 7:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*100000
			print(f"\nEl resultado es = {total}ml")
			
			
			
                                                                           			
			
#Dal a..
	#Dal a kl
		elif valor_1 ==3 and valor_2 == 1:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/100
			print(f"\nEl resultado es = {total}Kl")
	
	#Dal a hl
		elif valor_1 ==3 and valor_2 == 2:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10
			print(f"\nEl resultado es = {total}Hl")			

	#Dal a Dal
		elif valor_1 ==3 and valor_2 == 3:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1
			print(f"\nEl resultado es = {total}Dal")			
			
			
	#Dal a l
		elif valor_1 ==3 and valor_2 == 4:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10
			print(f"\nEl resultado es = {total}l")
			
	#Dal a dl
		elif valor_1 ==3 and valor_2 == 5:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*100
			print(f"\nEl resultado es = {total}dl")
						
	#Dal a cl
		elif valor_1 ==3 and valor_2 == 6:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1000
			print(f"\nEl resultado es = {total}cl")
			
	#Dal a ml
		elif valor_1 ==3 and valor_2 == 7:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10000
			print(f"\nEl resultado es = {total}ml")
			
						
                                                                           			
			
#l a..
	#l a kl
		elif valor_1 ==4 and valor_2 == 1:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/1000
			print(f"\nEl resultado es = {total}Kl")
	
	#l a hl
		elif valor_1 ==4 and valor_2 == 2:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/100
			print(f"\nEl resultado es = {total}Hl")			

	#l a Dal
		elif valor_1 ==4 and valor_2 == 3:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10
			print(f"\nEl resultado es = {total}Dal")			
			
			
	#l a l
		elif valor_1 ==4 and valor_2 == 4:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1
			print(f"\nEl resultado es = {total}l")
			
	#l a dl
		elif valor_1 ==4 and valor_2 == 5:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10
			print(f"\nEl resultado es = {total}dl")
						
	#l a cl
		elif valor_1 ==4 and valor_2 == 6:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*100
			print(f"\nEl resultado es = {total}cl")
			
	#l a ml
		elif valor_1 ==4 and valor_2 == 7:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1000
			print(f"\nEl resultado es = {total}ml")
			
			

                                                                           			
			
#dl a..
	#dl a kl
		elif valor_1 ==5 and valor_2 == 1:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10000
			print(f"\nEl resultado es = {total}Kl")
	
	#dl a hl
		elif valor_1 ==5 and valor_2 == 2:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/1000
			print(f"\nEl resultado es = {total}Hl")			

	#dl a Dal
		elif valor_1 ==5 and valor_2 == 3:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/100
			print(f"\nEl resultado es = {total}Dal")			
			
			
	#dl al
		elif valor_1 ==5 and valor_2 == 4:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10
			print(f"\nEl resultado es = {total}l")
			
	#dl a dl
		elif valor_1 ==5 and valor_2 == 5:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1
			print(f"\nEl resultado es = {total}dl")
						
	#dl a cl
		elif valor_1 ==5 and valor_2 == 6:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10
			print(f"\nEl resultado es = {total}cl")
			
	#dl a ml
		elif valor_1 ==5 and valor_2 == 7:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*100
			print(f"\nEl resultado es = {total}ml")
			
			
			
                                                                           			
			
#cl a..
	#cl a kl
		elif valor_1 ==6 and valor_2 == 1:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/100000
			print(f"\nEl resultado es = {total}Kl")
	
	#cl a hl
		elif valor_1 ==6 and valor_2 == 2:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10000
			print(f"\nEl resultado es = {total}Hl")			

	#cl a Dal
		elif valor_1 ==6 and valor_2 == 3:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/1000
			print(f"\nEl resultado es = {total}Dal")			
			
			
	#cl a l
		elif valor_1 ==6 and valor_2 == 4:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/100
			print(f"\nEl resultado es = {total}l")
			
	#cl a dl
		elif valor_1 ==6 and valor_2 == 5:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10
			print(f"\nEl resultado es = {total}dl")
						
	#cl a cl
		elif valor_1 ==6 and valor_2 == 6:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1
			print(f"\nEl resultado es = {total}cl")
			
	#cl a ml
		elif valor_1 ==6 and valor_2 == 7:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*10
			print(f"\nEl resultado es = {total}ml")
	
			
			
                                                                           			
			
#ml a..
	#ml a kl
		elif valor_1 ==7 and valor_2 == 1:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/1000000
			print(f"\nEl resultado es = {total}Kl")
	
	#ml a hl
		elif valor_1 ==7 and valor_2 == 2:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/100000
			print(f"\nEl resultado es = {total}Hl")			

	#ml a Dal
		elif valor_1 ==7 and valor_2 == 3:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10000
			print(f"\nEl resultado es = {total}Dal")			
			
			
	#ml a l
		elif valor_1 ==7 and valor_2 == 4:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/1000
			print(f"\nEl resultado es = {total}l")
			
	#ml a dl
		elif valor_1 ==7 and valor_2 == 5:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/100
			print(f"\nEl resultado es = {total}dl")
						
	#ml a cl
		elif valor_1 ==7 and valor_2 == 6:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero/10
			print(f"\nEl resultado es = {total}cl")
			
	#ml a ml
		elif valor_1 ==7 and valor_2 == 7:
			numero = float(input("\nIntroduce la cantidad que deseas cambiar : "))
			total = numero*1
			print(f"\nEl resultado es = {total}ml")				
			
			
			
			
# VELOCIDAD m/s km/h

	if seleccion == 5 :
		print("\nHas seleccionado 'Velocidad'")
		print("\n1. m/s a km/hora")
		print("2. km/hora a m/s")
		
		opcion= int(input("\nSeleccione que desea convertir : "))
		
		while opcion <=0 or opcion>=3:
			print("\nOpción no disponible , intentelo de nuevo")
			opcion= int(input("\nSeleccione que desea convertir : "))
			
		if opcion == 1:
			cantidad= float(input("\nCuantos m/s quiere convertir a Km/h :"))
			total = cantidad*3.6
			print(f"\ El resultado es {total:.2f}Km/h .")
		
		elif opcion == 2:
			cantidad= float(input("\nCuantos km/h quiere convertir a m/s :"))
			total = cantidad/3.6
			print(f"\nEl resultado es {total:.2f}m/s .")		
			
			
			
#Tiempo   año,mes,sem,dia,hora,min,seg 

	elif seleccion == 6:
		
		print("\nHas seleccionado 'Tiempo'")
		print("\n1. Dia")
		print("2. Hora")
		print("3. Minuto")
		print("4. Segundo")
		
		opcion = int(input("\nSelecciona la unidad que quieres convertir : "))
		while opcion <=0 or opcion>=5:
			print("\nOpción no disponible , intentalo de nuevo.")
			opcion = int(input("\nSelecciona la unidad que quieres convertir : "))
			
			
		opcion_2 = int(input("\nSelecciona a que unidad quieres converirlo : "))
		
		while opcion_2 <=0 or opcion_2 >=5:
			print("\nOpción no disponible , intentalo de nuevo.")
			opcion_2 = int(input("\nSelecciona la unidad que quieres convertir : "))
#DIAS
#dia a dia			
			
		if opcion == 1 and opcion_2 ==1:
			cuanto = float(input("\nIntroduce los dias que quieres pasar a dias :"))
			total = cuanto*1
			print(f"\nEl resultado es = {total} Dias.")

#dia a hora
			
		elif opcion == 1 and opcion_2 ==2:
			cuanto = float(input("\nIntroduce los dias que quieres pasar a horas :"))
			total = cuanto*24
			print(f"\nEl resultado es = {total} Dias.")

#dia a minuto	
		
		elif opcion == 1 and opcion_2 ==3:
			cuanto = float(input("\nIntroduce los dias que quieres pasar a minutos :"))
			total = cuanto*24*60
			print(f"\nEl resultado es = {total} Minutos.")
			
			
#dia a segundo

		elif opcion == 1 and opcion_2 ==4:
			cuanto = float(input("\nIntroduce los dias que quieres pasar a segundos :"))
			total = cuanto*24*60*60
			print(f"\nEl resultado es = {total} Segundos.")
#HORAS			
#hora a dia 

		elif opcion == 2 and opcion_2 ==1:
					cuanto = float(input("\nIntroduce las horas que quieres pasar a dias :"))
					total = cuanto/24
					print(f"\nEl resultado es = {total} Dias.")

#hora a hora
																			
		elif opcion == 2 and opcion_2 ==2:
					cuanto = float(input("\nIntroduce las horas que quieres pasar a horas :"))
					total = cuanto*1
					print(f"\nEl resultado es = {total} Horas.")

#horas a minutos

		elif opcion == 2 and opcion_2 ==3:
					cuanto = float(input("\nIntroduce las horas que quieres pasar a minutos :"))
					total = cuanto*60
					print(f"\nEl resultado es = {total} Minutos.")				
					
					
#horas a segundos

		elif opcion == 2 and opcion_2 ==4:
					cuanto = float(input("\nIntroduce las horas que quieres pasar a segundos :"))
					total = cuanto*60*60
					print(f"\nEl resultado es = {total} Segundos.")		
					
#MINUTOS						
	
#minuto a dia 

		elif opcion == 2 and opcion_2 ==1:
					cuanto = float(input("\nIntroduce los minutos que quieres pasar a dias :"))
					total = cuanto/60/24
					print(f"\nEl resultado es = {total} Dias.")

#minuto a hora
																			
		elif opcion == 2 and opcion_2 ==2:
					cuanto = float(input("\nIntroduce los minutos que quieres pasar a horas :"))
					total = cuanto/60
					print(f"\nEl resultado es = {total} Horas.")

#minuto a minutos

		elif opcion == 2 and opcion_2 ==3:
					cuanto = float(input("\nIntroduce los minutos que quieres pasar a minutos :"))
					total = cuanto*1
					print(f"\nEl resultado es = {total} Minutos.")				
					
					
#minuto a segundos

		elif opcion == 2 and opcion_2 ==4:
					cuanto = float(input("\nIntroduce los minutos que quieres pasar a segundos :"))
					total = cuanto*60
					print(f"\nEl resultado es = {total} Segundos.")		
													
					
					
#SEGUNDOS

#segundos a dia 

		elif opcion == 2 and opcion_2 ==1:
					cuanto = float(input("\nIntroduce los segundos que quieres pasar a dias :"))
					total = cuanto/60/60/24
					print(f"\nEl resultado es = {total} Dias.")

#segundos a hora
																			
		elif opcion == 2 and opcion_2 ==2:
					cuanto = float(input("\nIntroduce los segundos que quieres pasar a horas :"))
					total = cuanto/60/60
					print(f"\nEl resultado es = {total} Horas.")

#segundos a minutos

		elif opcion == 2 and opcion_2 ==3:
					cuanto = float(input("\nIntroduce los segundos que quieres pasar a minutos :"))
					total = cuanto/60
					print(f"\nEl resultado es = {total} Minutos.")				
					
					
#segundos a segundos

		elif opcion == 2 and opcion_2 ==4:
					cuanto = float(input("\nIntroduce los segundos que quieres pasar a segundos :"))
					total = cuanto*1
					print(f"\nEl resultado es = {total} Segundos.")		
													
					
					
					
#ALMACENAMIENTO  Tb,Gb,Mb,Kb,B,bit 
	elif seleccion ==7:
		print("\nHas seleccionado 'Almacenamiento'")
		print("\n1. Terabyte")
		print("2. Gigabyte")
		print("3. Megabyte")
		print("4. Kilobyte")
		print("5. Byte")

		
		opcion = int(input("\nSelecciona la unidad que quieres convertir : "))

		while opcion<=0 or opcion >=6:
			print("\nOpción no valida , intentelo de nuevo.")
			opcion = int(input("\nSelecciona la unidad que quieres convertir : "))


		opcion_2 = int(input("\nSelecciona a que unidad quieres convertirlo : "))

		while opcion_2 <=0 or opcion_2 >=6:
			print("\nOpción no valida , intentelo de nuevo.")
			opcion_2 = int(input("\nSelecciona a que unidad quieres convertirlo : "))
#tb a tb	
		if opcion ==1 and opcion_2 == 1:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad*1
			print(f"\nEl resultado es = {total}Tb.")
			
			
#tb a Gb	
		if opcion ==1 and opcion_2 == 2:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad*1024
			print(f"\nEl resultado es = {total}Gb.")
					

#tb a Mb	
		if opcion ==1 and opcion_2 == 3:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad*1024*1024
			print(f"\nEl resultado es = {total}Mb.")
			
			
#tb a kb	
		if opcion ==1 and opcion_2 == 4:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad*1024*1024*1024
			print(f"\nEl resultado es = {total}Kb.")
			

#tb a byte	
		if opcion ==1 and opcion_2 == 5:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad*1024*1024*1024*1024
			print(f"\nEl resultado es = {total}Bytes.")
			
			
			
			
#Gb a tb	
		if opcion ==2 and opcion_2 == 1:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad/1024
			print(f"\nEl resultado es = {total}Tb.")
			
			
#Gb a Gb	
		if opcion ==2 and opcion_2 == 2:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad*1
			print(f"\nEl resultado es = {total}Gb.")
					

#Gb a Mb	
		if opcion ==2 and opcion_2 == 3:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad*1024
			print(f"\nEl resultado es = {total}Mb.")
			
			
#Gb a kb	
		if opcion ==2 and opcion_2 == 4:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad*1024*1024
			print(f"\nEl resultado es = {total}Kb.")
			

#Gb a byte	
		if opcion ==2 and opcion_2 == 5:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad*1024*1024*1024
			print(f"\nEl resultado es = {total}Bytes.")





#Mb a tb	
		if opcion ==3 and opcion_2 == 1:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad/1024/1024
			print(f"\nEl resultado es = {total}Tb.")
			
			
#Mb a Gb	
		if opcion ==3 and opcion_2 == 2:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad/1024
			print(f"\nEl resultado es = {total}Gb.")
					

#Mb a Mb	
		if opcion ==3 and opcion_2 == 3:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad*1
			print(f"\nEl resultado es = {total}Mb.")
			
			
#Mb a kb	
		if opcion ==3 and opcion_2 == 4:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad*1024
			print(f"\nEl resultado es = {total}Kb.")
			

#Mb a byte	
		if opcion ==3 and opcion_2 == 5:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad*1024*1024
			print(f"\nEl resultado es = {total}Bytes.")
			
			
			
			
#Kb a tb	
		if opcion ==4 and opcion_2 == 1:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad/1024/1024/1024
			print(f"\nEl resultado es = {total}Tb.")
			
			
#Kb a Gb	
		if opcion ==4 and opcion_2 == 2:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad/1024/1024
			print(f"\nEl resultado es = {total}Gb.")
					

#kb a Mb	
		if opcion ==4 and opcion_2 == 3:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad/1024
			print(f"\nEl resultado es = {total}Mb.")
			
			
#Kb a kb	
		if opcion ==4 and opcion_2 == 4:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad*1
			print(f"\nEl resultado es = {total}Kb.")
			

#Kb a byte	
		if opcion ==4 and opcion_2 == 5:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad*1024
			print(f"\nEl resultado es = {total}Bytes.")
							
							
							
#byte a tb	
		if opcion ==5 and opcion_2 == 1:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad/1024/1024/1024/1024
			print(f"\nEl resultado es = {total}Tb.")
			
			
#byte a Gb	
		if opcion ==5 and opcion_2 == 2:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad/1024/1024/1024
			print(f"\nEl resultado es = {total}Gb.")
					

#byte a Mb	
		if opcion ==5 and opcion_2 == 3:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad/1024/1024
			print(f"\nEl resultado es = {total}Mb.")
			
			
#byte a kb	
		if opcion ==5 and opcion_2 == 4:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad/1024
			print(f"\nEl resultado es = {total}Kb.")
			

#byte a byte	
		if opcion ==5 and opcion_2 == 5:
			cantidad = float(input("\nIntroduce la cantidad que deseas convertir : "))
			total = cantidad*1
			print(f"\nEl resultado es = {total}Bytes.")
							
							
							
							
							
							
	elif seleccion == 8:
		print("\nHas seleccionado Velocidad|Tiempo")
		velocidad = int(input("\nIntroduce la velocidad 'km/h' : "))
		distancia = int(input("\nIntroduce la distancia 'km' :"))
		resultado_1 = velocidad/3.6#metros por segundo 
		resultado_2 = distancia/velocidad#tiempo en horas
	
		if resultado_2 <=1:
			resultado_2 = resultado_2*60
			print(f"\nLa velocidad en metros por segundo es = {resultado_1}")
			print(f"\nEl tiempo en recorrer los {distancia}km es de {resultado_2} minutos.")
		else:
			print(f"\nLa velocidad en metros por segundo es = {resultado_1}")
			print(f"\nEl tiempo en recorrer los {distancia}km es de {resultado_2} horas.")
