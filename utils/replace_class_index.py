for root, dirs, files in os.walk("."):
    for filename in files:
        
        modified_lines = []
        new_str = ''
        appended_str = ''
        
        
        if 'txt' in filename :
            with open(filename,'r+') as fin:
                lines = fin.readlines()
                
                for line in lines:
                    line_list = list(line)
                    line_list[0] = '3'
                    modified_lines.append(line_list)
                    
                
                fin.seek(0)
                fin.truncate()
                
                for new_line in modified_lines:
                    appended_str += new_str.join(new_line)
                
                fin.write(appended_str)