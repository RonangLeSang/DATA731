
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


def get_real_size(numFrame, numLine, image_width, image_height):
    x1, y1, x2, y2 = get_vector(numFrame, numLine, image_width, image_height)
    vertDist = x2 - x1
    horizDist = y2 - y1


get_vector(100, 6, 1080, 720)
