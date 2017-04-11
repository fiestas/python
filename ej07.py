frase="Estamos desarrollando un codigo en python"
letra="s"
k=0
for i in frase:
    if i==letra:
        k=k+1
        print("encontramos la letra ",letra," en la posición ",k+1)
        break
    else:
        print("buscando ...")




