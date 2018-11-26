import os
fo = open("./test.csv", "w+")
# print "Name of the file: ", fo.name
# print "Closed or not : ", fo.closed
# print "Opening mode : ", fo.mode
# print "Softspace flag : ", fo.softspace
# print "read: ", os.getcwd()
# fo = open("foo.txt", "wb")
# fo.write( "Python is a great language. Yeah its great!!");
# Close opend file
# fo.close()

with open('foo.txt', 'a') as file:
    file.seek(0)
    file.write('input')

def add_header(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

def stringifyCsv():
    print('in stringify')
    data=''
    with open('noheader.csv', 'r') as myfile:
        data=myfile.read()
    return data

def findMax():
    files = ["logs-2018-10-14-00.csv","logs-2018-10-14-01.csv","logs-2018-11-14-01.csv"]
    print(max(files))

# print stringifyCsv()
findMax()
