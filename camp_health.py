from health import HP


# создание массива
def arr_create_health(display):
    arr_set = [
        HP(display, "Effects/heart.png")
    ]
    array_hp = []
    for i in range(len(arr_set) * 1):
        array_hp.append(arr_set[i])
    return array_hp


# прорисовка всех сердечек
def array_draw_health(array_health, point):
    for health in array_health:
        health.draw(point)
