colors = ["Red", "Yellow", "Blue", "Green"]
colors_len = len(colors)

for i in range(0,colors_len):
    print("Before value of ", i, "is", colors[i])
    colors[i] = "White"
    print("After value of ", i , "is", colors[i])
    