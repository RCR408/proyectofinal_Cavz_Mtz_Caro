import LMC as lm

mnemonico = {"INP":"901","OUT":"902","LDA":"5","STA":"3","ADD":"1","SUB":"2","BRA":"6","BRZ":"7","BRP":"8","HLT":"000","DAT":"000"}


not_need_dir = ["INP","OUT","HLT","DAT"]
need_dir = ["LDA","STA","ADD","SUB","BRA","BRZ","BRP"]
def lmc(memoria,linea):
    file = open("solucion.txt","w")

    for i in range(0,100):
        if len(memoria)-1<i:
            file.write(str(i)+ "    " + "000" + "\n")
        else:
                if (mmnemico[memoria[i]]) in not_need_dir:
                    temp = linea.pop()
                    file.write(str(i)+ "    " + str(mmnemico[str(memoria[i])]) + str(temp) +"    " + str(memoria[i]) + "\n")
                else:
                    file.write(str(i)+ "    " + str(mmnemico[str(memoria[i])]) +"    " + str(memoria[i]) + "\n")

def primera_pasada(archivo):
    line = []
    index = []
    instruccion = ""
    temp_etiqueta = ""
    etiqueta = []

    memoria = list([])
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
            count +=1
            memoria.append(instruccion)
    return memoria, line,index

t = primera_pasada("prueba01.txt")
