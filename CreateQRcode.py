def Create():
    from termcolor2 import c
    print(c("""
 _____                     _         
/  __ \\                   | |        
| /  \\/ _ __   ___   __ _ | |_   ___ 
| |    | '__| / _ \\ / _` || __| / _ \\
| \\__/\\| |   |  __/| (_| || |_ |  __/
 \\____/|_|    \\___| \\__,_| \\__| \\___|
                                     """).blue.blink)
    print(c("\n\n|Enter The Data(Text, URL) That You Want To Make In To A QR Code:").magenta)
    data = str(input(c("    -->").red))
    import qrcode as qr
    qrCode = qr.make(data)
    print(c("\n|_/1.JPEG").yellow)
    print(c("|_/2.JPG").yellow)
    print(c("|_/3.PNG").yellow)
    print(c("    |Which Format Of Image You Want The QR Code To Be:").cyan)
    while True:
        try:
            data = int(input(c("      -->").red))
            if data == 1 or data == 2 or data == 3:
                break
            else:
                raise ValueError
        except:
            pass
    print(c("\n|Enter The Name Of The File:").magenta)
    name = str(input(c("    -->").red))
    if data == 1:
        qrCode.save(name + ".jpeg")
        print(c("Your QR Code Is Saved With Name Of " + name + ".jpeg").green)
    elif data == 2:
        qrCode.save(name + ".jpg")
        print(c("Your QR Code Is Saved With Name Of " + name + ".jpg").green)
    elif data == 3:
        qrCode.save(name + ".png")
        print(c("Your QR Code Is Saved With Name Of " + name + ".png").green)
