import LMC as lm

mnemonico = {"INP":"901","OUT":"902","LDA":"5","STA":"3","ADD":"1","SUB":"2","BRA":"6","BRZ":"7","BRP":"8","HLT":"000","DAT":"000"}


not_need_dir = ["901","902","000","000"]
need_dir = ["5","3","1","2","6","7","8"]

def segunda_pasada(memoria,linea,index,file):
    save = len(memoria)
    file = open(file,"w")
    dir = []

    for e in range(0,len(index)):
        dir.append(save+e)

    for i in range(0,100):
        if i<len(memoria):
            if (mnemonico[str(memoria[i])]) in not_need_dir:
                file.write(str(i)+ "    " + str(mnemonico[str(memoria[i])]) +"    " + str(memoria[i]) + "\n")

            if (mnemonico[str(memoria[i])]) in need_dir:
                if i in linea:
                    file.write(str(i)+ "    " + str(mnemonico[str(memoria[i])]) + str(dir[index[linea.index(i)]]).zfill(2) +"    " + str(memoria[i]) + "\n")
        else:
            file.write(str(i)+ "    " + "000" +"    " + "\n")

def primera_pasada(archivo):
    line = []
    index = []
    instruccion = ""
    temp_etiqueta = ""
    etiqueta = []

    memoria = [] 
    count = 0
    with open(archivo) as file:
        for linea in file:
            linea = linea.replace(" ","",5)
            partes = linea.strip().split(' ')
            if len(partes)>1:
                if partes[1] in mnemonico:
                    instruccion = partes[1]
                    temp_etiqueta = partes[0]
                if partes[0] in mnemonico:
                    instruccion = partes[0]
                    temp_etiqueta = partes[1]

                if len(etiqueta)>0:
                    if temp_etiqueta not in etiqueta:
                        etiqueta.append(temp_etiqueta)
                else:
                    etiqueta.append(temp_etiqueta)
                line.append(count)  
                index.append(etiqueta.index(temp_etiqueta))
            else:
                instruccion = partes[0]
            memoria.append(instruccion)
            count +=1
    return memoria, line,index

m,l,i = primera_pasada("programa1.txt")
segunda_pasada(m,l,i,"solucion.txt")
leer=lm.leertxt("solucion.txt")
print(lm.ejecutar_lmc(leer,[2,5]))

m1,l1,i1 = primera_pasada("programa2.txt")
segunda_pasada(m1,l1,i1,"solucion2.txt")
leer=lm.leertxt("solucion2.txt")
print(lm.ejecutar_lmc(leer,[7,5]))

m2,l2,i2 = primera_pasada("programa3.txt")
segunda_pasada(m2,l2,i2,"solucion3.txt")
leer=lm.leertxt("solucion3.txt")
print(lm.ejecutar_lmc(leer,[2,5]))