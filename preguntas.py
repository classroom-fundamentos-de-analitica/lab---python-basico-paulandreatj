"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    file = open("data.csv", "r")
    values = [int(line[2]) for line in file]
    file.close()
    return sum(values)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    file = open("data.csv", "r")
    l = [line[0] for line in file]
    r = sorted((letra, l.count(letra)) for letra in set(l))

    return r


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    file = open("data.csv", "r")
    values = [(line[0], line[2]) for line in file]
    file.close()
    result = {}
    for letra, num in values:
        if letra not in result:
            result[letra] = int(num)
            continue
        result[letra] += int(num)

    return sorted((key, value) for key, value in result.items())


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    file = open("data.csv", "r")
    meses = [line[9:11] for line in file]
    file.close()
    result = sorted((mes, meses.count(mes)) for mes in set(meses))

    return result


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    file = open("data.csv", "r")
    ingress = [(line[0], int(line[2])) for line in file]
    file.close()
    l = set([ent[0] for ent in ingress])
    result = []
    for letra in l:
        lIngress = []
        for ent in ingress:
            if ent[0] == letra:
                lIngress.append(ent[1])
        result.append((letra, max(lIngress), min(lIngress)))
    return sorted(result)


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    strings = []
    values = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            dicti = fila[4].split(',')

            for e in dicti: 
                cadena = e.split(':')[0]
                valor = e.split(':')[1]

                if cadena not in strings:
                    strings.append(cadena)
                    values.append([int(valor)])
                else:
                    values[strings.index(cadena)].append(int(valor))

    output = []

    for cadena in sorted(strings):
        output.append((cadena, min(values[strings.index(cadena)]), max(values[strings.index(cadena)])))

    return output


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    file = open("data.csv", "r")
    ingress = [(int(line[2]), line[0]) for line in file]
    file.close()
    values = set([tupla[0] for tupla in ingress])
    ans = []
    for value in values:
        ans.append((value, [tupla[1] for tupla in ingress if tupla[0] == value]))
    return sorted(ans)


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            if int(fila[1]) not in nums:
                nums.append(int(fila[1]))
                l.append({fila[0]})
            else:
                l[nums.index(int(fila[1]))].add(fila[0])

    output = []

    for numero in sorted(nums):
        output.append((numero, list(sorted(l[nums.index(numero)]))))

    return output


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    file = open("data.csv", "r")
    ingress = [line.split(",")[1:] for line in file]
    file.close()
    ingressDict = []
    for lista in ingress:
        for entrada in lista:
            if len(entrada) > 1:
                sublist = entrada.strip().split("\t")
                if len(sublist) > 1:
                    ingressDict.append(sublist[1][:3])
                    continue
                ingressDict.append(sublist[0][:3])
    ans = {key:ingressDict.count(key) for key in ingressDict}

    return ans


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    f = open("data.csv", "r")
    entradas = [line.split("\t") for line in f]
    f.close()
    resultado = []
    for entrada in entradas:
        letra = entrada[0]
        columna4 = entrada[3].split(",")
        columna5 = ",".join(entrada[4:]).split(",")
        resultado.append((letra, len(columna4), len(columna5)))

    return resultado


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    letras = {}
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            for letra in row[3].split(","):
                if(not letra in letras.keys()):
                    letras.update({letra: int(row[1])})
                else:
                    letras[letra] += int(row[1])
    dicc = sorted(letras.items())
    return dict(dicc)


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    letras = {}
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='	')
        for row in csv_reader:
            letra = row[0]
            for codigo in row[4].split(","):
                numero = int(codigo.split(":")[1])
                if(not letra in letras.keys()):
                    letras.update({letra: numero})
                else:
                    letras[letra] += numero
    dicc = sorted(letras.items())
    return dict(dicc)
