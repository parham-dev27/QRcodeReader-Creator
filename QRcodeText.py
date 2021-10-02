from StartTemplateQRcode import startTemplate
num_given = startTemplate()
if num_given == 1:
    from CreateQRcode import Create
    Create()
elif num_given == 2:
    from ReadQRcode import Read
    Read()