def sum(conj):
    sum = 0
    for value in range(len(conj)):
        sum = sum + conj[value]
    return sum

def sum_products(conj_x, conj_y):
    sum = 0
    for value in range(len(conj_x)):
        sum = sum + (conj_x[value] * conj_y[value])
    return sum

def sum_square(conj):
    sum = 0
    for value in range(len(conj)):
        sum = sum + (conj[value]**2)
    return sum

def inclination(conj_x, conj_y):
    n_elements = len(conj_x)

    return ((n_elements * sum_products(conj_x, conj_y)) - (sum(conj_x)* sum(conj_y))) / ((n_elements * sum_square(conj_x))- (sum(conj_x)**2))

def interception(conj_x, conj_y):
    n_elements = len(conj_x)

    x = sum(conj_x) / n_elements
    y = sum(conj_y) / n_elements

    return y - (inclination(conj_x, conj_y) * x)

def interpolate(conj_x, conj_y, value):
    return interception(conj_x, conj_y) + (inclination(conj_x, conj_y) * value)

conj_y = [30.1, 40.5, 51, 61.1, 71.2]
conj_x = [30, 40, 50, 60, 70]

value = 39


#valor lido = conj_y
#valor referência = conj_x

print(interpolate(conj_x, conj_y, value))