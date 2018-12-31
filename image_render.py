from PIL import Image as img


def image_render(name):
    image = img.open('Sprites/%s/text.png' % name)
    pix = image.load()

    width = image.size[0]
    height = image.size[1]

    for i in range(width):
        for j in range(height):
            if sum(pix[i, j]) != 255:
                pix[i, j] = (255, 255, 255, 255)

    image.save('Sprites/%s/text1.png' % name)