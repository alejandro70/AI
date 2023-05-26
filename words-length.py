with open("palabras.txt",'r',encoding='utf8') as f:
    words = f.read().split()

while True:
    n = int(input("\nIntroduce la longitud de las palabras que quieres ver: "))

    # Filtramos las palabras que tienen la longitud deseada
    selected_words = [word for word in words if len(word) == n]

    # Ordenamos las palabras alfabéticamente
    selected_words = sorted(selected_words)

    # Mostramos las palabras en columnas
    num_cols = 5
    num_rows = -(-len(selected_words) // num_cols)  # Round up division
    for i in range(num_rows):
        for j in range(num_cols):
            index = i + j * num_rows
            if index < len(selected_words):
                print("{:<15}".format(selected_words[index]), end='')
        print()  # Start a new row
