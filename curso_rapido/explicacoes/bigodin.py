bigode = 'mustache'
bigodin = bigode

del bigode

# bigodin ainda aponta para 'mustache'
print(bigodin)

del bigodin

# objeto destruido
# print(bigodin)
# print(bigode)
