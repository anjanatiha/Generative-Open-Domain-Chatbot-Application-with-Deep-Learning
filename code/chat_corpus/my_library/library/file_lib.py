import os

# reads file
def read_file(filename):             
    with open(filename, 'r') as content_file:
        content = content_file.read()
    return content


# reads file line by line/ splits by line
def read_file_lines(filename):             
    with open(filename, 'r') as content_file:
        content = content_file.readlines()
    return content


# writes file whole content
def write(filename, content):
    fh = open(filename,"w")
    fh.write(content)
    fh.close()


# appends to file whole content
def append(filename, content):
    fh = open(filename,"a")
    fh.write(content)
    fh.close()


# writes file in reverse
def reverse_write_file(filename):
    output_file = filename
    if filename[len(filename)-4:] == ".txt":
        output_file = filename[:len(filename)-4]
    output_file = output_file + "_reverse.txt"

    fh = open(output_file,"w")
    for line in reversed(list(open(filename))):
        fh.write(line)
    fh.close()
    return output_file


