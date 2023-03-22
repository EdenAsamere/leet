def interpret(command):
    if '()' in command:
        command = command.replace('()','o')
    elif '(al' in command:
        command = command.replace('(','')
    elif 'al)' in command:
        command = command.replace(')','')
    return command
        
        
   
command = "G()()(al)"
print(interpret(command))
