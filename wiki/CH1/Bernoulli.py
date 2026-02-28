# -------------------------------------------
# -- Numeros de Bernoulli
# -------------------------------------------

# -- Numero maximo de Bernoulli a obtener
N = 14

# -- Lista para almacenar los numeros
A = [0.0] * (N+2)

print("Numeros de Bernoulli")
print("--------------------")
for m in range(N+1):
    A[m+1] = 1 / (m+1)

    # -- Barrido hacia atras
    for j in range(m + 1, 1, -1):
        A[j-1] = (j-1) * (A[j-1] - A[j])

    # -- A(1) es Bm
    if m == 1 or m % 2 == 0:
        print(f"B{m}={A[1]}")

print("--------------------\n")
