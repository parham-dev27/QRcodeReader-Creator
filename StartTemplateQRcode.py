def startTemplate():
    from termcolor2 import c
    while True:
        print(c("""           ____    _____                       _        
              / __ \\  |  __ \\                     | |       
             | |  | | | |__) |   ___    ___     __| |   ___ 
             | |  | | |  _  /   / __|  / _ \\   / _` |  / _ \\
             | |__| | | | \\ \\  | (__  | (_) | | (_| | |  __/
              \\___\\_\\ |_|  \\_\\  \\___|  \\___/   \\__,_|  \\___|
                                                    
                                                    """).blue.blink)
        print(c("\n\n|_/1.CREATE").green.bold)
        print(c("|_/2.SCAN").green.bold)
        print(c("   |Enter 1 For Creating A QRcode Or 2 For Scanning A Image:").cyan)
        num = input(c("       -->").red)
        try:
            num = int(num)
        except:
            pass
        if num == 1 or num == 2:
            return num


