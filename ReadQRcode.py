def Read():
    import cv2
    from termcolor2 import c
    print(c("""
    ______                   _  
    | ___ \\                 | | 
    | |_/ /  ___   __ _   __| | 
    |    /  / _ \\ / _` | / _` | 
    | |\\ \\ |  __/| (_| || (_| | 
    \\_| \\_| \\___| \\__,_| \\__,_|                        
        """).blue.blink)
    print(c("\n\n|Enter The Files Name/Path:").yellow)
    filename = input(c("    -->").red)
    image = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    try:
        data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
        if vertices_array is not None:
            print(c("Data is:").magenta)
            print(c(data).green)
        else:
            print(c("\\\\Something Went Wrong!").red)
    except:
        print(c("\\\\Something Went Wrong!").red)
