from PIL import Image as img

def pars(im):
    lab = img.open(im)
    width = lab.size[0]
    height = lab.size[1]
    pix = lab.load()
    return_lab = []
    small_width = True
    small_height = True

    i, j = 0, 0
    while i < height:
        s = ''
        j = 0
        while j < width:
            a = pix[j, i][0]
            b = pix[j, i][1]
            c = pix[j, i][2]
            S = (a + b + c)
            if S == 0:
                s += '*'
            else:
                s += ' '

            if small_width:
                j += 2
                small_width = False
            else:
                j += 14
                small_width = True

        if small_height:
            i += 2
            small_height = False
        else:
            i += 14
            small_height = True

        return_lab.append(s)
    return return_lab