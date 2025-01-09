import sys,math, requests
from PIL import Image

def clampWithAdjustment(num,min, max):
    if num <= min: return min
    if num >= max: return max
    
    return num


brightnessScale = " `.-\':_,^=;><+!rc*/z?sLTv)J7(|Fi{{C}}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
print(len(brightnessScale))
imgPath = sys.argv[1]
initUrl = requests.get(imgPath).content
with open("./baseImage.jpg", "wb") as file: file.write(initUrl)
image = Image.open("./baseImage.jpg").convert("RGB")
width, height = image.size
delimiter = int(sys.argv[2])
image = image.resize((width//delimiter, height//delimiter))
width, height = image.size

with open("./output.txt","w") as file:
    for row in range(height):
        for col in range(width):
            r,g,b = image.getpixel((col,row))
            brightness = clampWithAdjustment(math.ceil(0.299*r + 0.587*g + 0.114*b),1,len(brightnessScale))
            # print(brightness/len(brightnessScale))
            # print(brightnessScale[brightness-1]*3)
            file.write(brightnessScale[brightness-1]*3)
        file.write("\n")
    file.close()