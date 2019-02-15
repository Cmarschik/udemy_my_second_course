with open("my_file.txt", 'w') as f: #this opens file and ensures that it will close once finished
    #use 'w' to write in the file / use 'r' to read from the file / others as well
    #opens file as writing type with a file name of 'f'
    #'With' allows the computer to automatically close the file once we have left the parameters of this indention
    f.write('Hello World!') #writes in new file(created automaticaly)
    f.write('\nHello World 2!')

with open("my_file.txt", 'r') as f: #this opens file and ensures that it will close once finished
    #use 'w' to write in the file / use 'r' to read from the file / others as well
    #opens file as writing type with a file name of 'f'
    #'With' allows the computer to automatically close the file once we have left the parameters of this indention
    print(f.read()) #prints the text from the new file just written in

