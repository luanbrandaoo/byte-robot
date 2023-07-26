from PIL import Image
from time import sleep

def convert_to_r5g6b5(pixel):
    r, g, b = pixel[0], pixel[1], pixel[2]

    r5 = (r >> 3) & 0x1F
    g6 = (g >> 2) & 0x3F
    b5 = (b >> 3) & 0x1F

    pixel_16bits = (r5 << 11) | (g6 << 5) | b5

    return pixel_16bits

def image_to_pixel_list(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")

    pixel_list = list(img.getdata())

    pixel_list_16bits = [convert_to_r5g6b5(pixel) for pixel in pixel_list]

    return pixel_list_16bits

def send_image(s,image_path):
    while 1:
        s.write("send_image".encode())
        print('esperando ok')

        if str(s.readline().decode()).strip() == 'ok':
            print('ok')
            break

    pixel_list_16bits = image_to_pixel_list(image_path)

    print("Enviando imagem...")

    p = 0
    x = 0
    y = 0

    for pixel in pixel_list_16bits:
        if pixel == 0:
            p=p+1
            continue

        y = (p//160)
        x = (p%160)

        s.write(f"{x:03},{y:03},{pixel:04x}\n".encode())
        print(f"{x:03},{y:03},{pixel:04x}\n")
        p=p+1
    
    while 1:
        s.write("XXXX".encode())
        if str(s.readline().decode()).strip() == 'end':
            print("Envio finalizado")
            break 

if __name__ == "__main__":
    import serial
    s = serial.Serial('COM4', 150000, timeout=5)
    
    send_image(s,"testimg.png")
