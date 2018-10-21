import mipow

# $ sudo hcitool lescan
bulb = mipow.mipow("14:87:4B:11:AC:E6")
# bulb.connect()

# status = bulb.get_state()
# bulb.on()
# bulb.set_rgb(255, 123, 0)
bulb.set_effect(white = 0, red = 255, green = 123, blue = 0, mode = 4, speed = 10)
# bulb.off()
