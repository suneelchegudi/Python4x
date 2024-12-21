colors = ["Red", "Yellow", "Blue", "Green"]

i = 0
selected_color = colors[0]

while(selected_color != 'Green'):
    print(selected_color)
    i = i + 1
    selected_color = colors[i]

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'blue'):
    new_squares.append(squares[i])
    i = i + 1
print(new_squares)