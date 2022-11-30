with open("emotion.txt", "r") as fh: #Insert name of txt image file here.
    data = fh.read().split(',') #open file and read it with split comma

column = 32; #Set column value

def dmd_function():
    print("\n")
    for index, state in enumerate(data, start=0): #Loop through list
        row = (index)//column; #// will floor the number.

        if index < column:
            print("dmd.writePixel(" + format(index) + "," + format(row) + ",GRAPHICS_NORMAL," + state + ");", end='') 
        elif index < column*2:
            print("dmd.writePixel(" + format(index-column) + "," + format(row) + ",GRAPHICS_NORMAL," + state + ");", end='')
        elif index < column*3:
            print("dmd.writePixel(" + format(index-column*2) + "," + format(row) + ",GRAPHICS_NORMAL," + state + ");", end='')
        elif index < column*4:
            print("dmd.writePixel(" + format(index-column*3) + "," + format(row) + ",GRAPHICS_NORMAL," + state + ");", end='')
        elif index < column*5:
            print("dmd.writePixel(" + format(index-column*4) + "," + format(row) + ",GRAPHICS_NORMAL," + state + ");", end='')
        elif index < column*6:
            print("dmd.writePixel(" + format(index-column*5) + "," + format(row) + ",GRAPHICS_NORMAL," + state + ");", end='')
        elif index < column*7:
            print("dmd.writePixel(" + format(index-column*6) + "," + format(row) + ",GRAPHICS_NORMAL," + state + ");", end='')
        elif index < column*8:
            print("dmd.writePixel(" + format(index-column*7) + "," + format(row) + ",GRAPHICS_NORMAL," + state + ");", end='')
        elif index < column*9:
            print("dmd.writePixel(" + format(index-column*8) + "," + format(row) + ",GRAPHICS_NORMAL," + state + ");", end='')
        elif index < column*10:
            print("dmd.writePixel(" + format(index-column*9) + "," + format(row) + ",GRAPHICS_NORMAL," + state + ");", end='')
        elif index < column*11:
            print("dmd.writePixel(" + format(index-column*10) + "," + format(row) + ",GRAPHICS_NORMAL," + state + ");", end='')
        elif index < column*12:
            print("dmd.writePixel(" + format(index-column*11) + "," + format(row) + ",GRAPHICS_NORMAL," + state + ");", end='')
        elif index < column*13:
            print("dmd.writePixel(" + format(index-column*12) + "," + format(row) + ",GRAPHICS_NORMAL," + state + ");", end='')
        elif index < column*14:
            print("dmd.writePixel(" + format(index-column*13) + "," + format(row) + ",GRAPHICS_NORMAL," + state + ");", end='')
        elif index < column*15:
            print("dmd.writePixel(" + format(index-column*14) + "," + format(row) + ",GRAPHICS_NORMAL," + state + ");", end='')
        elif index < column*16:
            print("dmd.writePixel(" + format(index-column*15) + "," + format(row) + ",GRAPHICS_NORMAL," + state + ");", end='')
    print("\n")
                
dmd_function()
fh.close()


