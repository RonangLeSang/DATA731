
def convert_coordinates(x_center, y_center, width, height, image_width, image_height):
    x_center *= image_width
    y_center *= image_height
    width *= image_width
    height *= image_height

    x1 = int(x_center - width / 2)
    y1 = int(y_center - height / 2)
    x2 = int(x_center + width / 2)
    y2 = int(y_center + height / 2)

    return x1, y1, x2, y2


def format_name(number):
    model = "{0:0003}"
    return model.format(number)


def get_vector(numFrame, numLine, image_width, image_height):
    with open(f"train/labels/frame_0{format_name(numFrame)}.txt", "r") as f:
        x_center, y_center, width, height = f.read().split("\n")[numLine].split(" ")[1:]
    return convert_coordinates(float(x_center), float(y_center), float(width), float(height), image_width, image_height)


def get_pixel_size(numFrame, numLine, image_width, image_height):
    coord = get_vector(numFrame, numLine, image_width, image_height)
    return [(coord[2] - coord[0]), (coord[3] - coord[1])], int(coord[1] + coord[3] / 2)


def set_scale(numFrame, numLine, image_width, image_height, scale):
    scale.append(get_pixel_size(numFrame, numLine, image_width, image_height))
    return scale


def get_ends_of_car(size, center):
    return [center + size[1]/2, center - size[1]/2]


def get_pixel_distance(size1, center1, size2, center2):
    car1 = get_ends_of_car(size1, center1)
    car2 = get_ends_of_car(size2, center2)
    return min([car1[0] - car2[1], car1[1] - car2[0]])


def get_real_size(numFrame, numLine, image_width, image_height):
    size, center = get_pixel_size(numFrame, numLine, image_width, image_height)
    return size, center


get_vector(100, 6, 1080, 720)
print(set_scale(100, 6, 1080, 720, set_scale(105, 6, 1080, 720, [])))
size1, center1 = get_real_size(100, 5, 1080, 720)
size2, center2 = get_real_size(100, 6, 1080, 720)
print(f"taille : {size1}, centre : {center1}")
print(get_pixel_distance(size1, center1, size2, center2))
