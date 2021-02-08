# 
for root, dirs, files in os.walk("."):
    for filename in files:
        if 'xml' in filename:
            # print(filename)
            os.rename(filename,filename.replace('.xml',''))

