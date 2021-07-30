file2 = open("train.txt", 'w')
file3 = open("test.txt", 'w')
    ("data/obj"+file)


percentage_test = 10
index_test = round(100 / percentage_test)


a = file1.readlines()
counter = 1
for file in a:
    if file[-2] == 'g':
        if(counter == index_test):
            counter = 1
            file3.write(file) 
        else:
            file2.write(file)
            counter = counter + 1

        
    
    

