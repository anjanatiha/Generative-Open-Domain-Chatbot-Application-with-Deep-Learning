import re
import time
import time_lib
import codecs

#import sys
#reload(sys)
#sys.setdefaultencoding('UTF-8')


# cornel movie files

# read file line by line/ splits by line
def read_file_line_by_line(filename):   
    with open(filename, "r") as content_file:
        content = content_file.readlines()
    return content


def write(filename, content):
    fh = open(filename,"w")
    fh.write(content)
    fh.close()

# extract sequence after last occurance
def extract_line_af(line, symbol_seq):
    return line.rsplit(symbol_seq)[-1]

# extract sequence after last occurance for multiple lines
def extract_line_af_all(content, symbol_seq):
    for line in content:
    	line_ex = extract_line_af(line, symbol_seq)
    	print(line_ex)

# reads file in reverse
def read_file_line_by_line_reverse(filename):
    for line in reversed(list(open(filename))):
    	print(line)


# converts text to lowercase
def to_lower(text):
    return text.lower()

# removes all spaces 
# replaces " " with ""
def remove_all_space(text):
    return re.sub(r' +', '', text)

# removes multiple spaces with single space
def remove_multi_space(text):
    return re.sub(r' +', ' ', text)

# add space before and after the punctuation
def add_space_punc(text):
    return re.sub("([^a-zA-Z0-9])", r' \1 ', text)

# remove all the characters except alphabetical
# removes special characters and numerical charcharters
def remove_non_alpha(text):
    return re.sub(r'[^a-zA-Z]', ' ', text)

# splits stiong by space or " "
def split_string(text):
    return text.split()


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

# writes file in reverse and extract sequence after last occurance for multiple lines
def reverse_write_file_extract(filename):
    output_file = filename
    if filename[len(filename)-4:] == ".txt":
        output_file = filename[:len(filename)-4]
    output_file = output_file + "_reverse.txt"

    fh = open(output_file,"w")
    for line in reversed(list(open(filename))):
        line_ex = extract_line_af(line, symbol_seq)
        fh.write(line_ex)
    fh.close()
    return output_file



# reads in reverse and extract sequence after last occurance for multiple lines
def extract_line_af_all(filename, symbol_seq):
    for line in reversed(list(open(filename))):
    	line_ex = extract_line_af(line, symbol_seq)
    	print(line_ex)




def get_vocab(filename):
    print(" Getting vocabulory from file: \"%s\" ........."%filename)
    word_vocab = {}
    content = read_file_line_by_line(filename)
    for line in content:
	line = line.strip()
	line = add_space_punc(line)
	line = remove_multi_space(line)
	tokens = split_string(line)
	for word in tokens:
	    word = word.strip()
	    if word not in word_vocab:
		word_vocab[word] = 1
	    else:
		word_vocab[word] +=1

    return word_vocab

def write_dict2(filename, vocab_dict, type_p):
    print("Writing dictionary to file: \"%s\" (%s) ........." % (filename, type_p))
    output_file = filename
    #if filename[len(filename)-4:] == ".txt":
    #    output_file = filename[:len(filename)-4]
    #output_file = output_file + "_vocab.txt"
    

    print(" Vocab length: %s"% len(vocab_dict))
    fh = open(output_file,"w")
    if type_p == "key":
       i = 0 
       for word in vocab_dict:
	   fh.write(word)
	   i +=1
	   if i %10000 == 0:
	      print("Index: %s" % (i))
    else:
       i = 0 
       for word in vocab_dict:
	   fh.write(word, vocab_dict[word])
	   i +=1
	   if i %10000 == 0:
	      print("Index: %s" % (i))
    fh.close()
    return output_file

def write_dict(filename, vocab_dict, type_p):
    print("Writing dictionary to file: \"%s\" (%s) ........." % (filename, type_p))
    output_file = filename
    print(" Vocab length: %s"% len(vocab_dict))
    fh = open(output_file,"w")
    buffer_str = ""
    if type_p == "key":
       i = 0 
       for word in vocab_dict:
	   if buffer_str == "":
	   	buffer_str = word
	   else:
		buffer_str = buffer_str + "\n" + word
	   i +=1
	   if i %10000 == 0:
	      fh.write(buffer_str)
	      buffer_str = ""
	      print("Index: %s" % (i))
    else:
       i = 0 
       for word in vocab_dict:
	   if buffer_str == "":
	   	buffer_str = word + " , "+ vocab_dict[word]
	   else:
		buffer_str = buffer_str + "\n" + word + " , "+ vocab_dict[word]
	   
	   i +=1
	   if i %10000 == 0:
	      fh.write(buffer_str)
	      buffer_str = ""
	      print("Index: %s" % (i))
    fh.close()
    return output_file


def dialouge_extract(input_file1, input_file2, max_dialouge_count, output_file1, output_file2):
	content1 = read_file_line_by_line(input_file1)
	content2 = read_file_line_by_line(input_file2)
	dialouge_count = 0
	fh1 = open(output_file1,"w")
	fh2 = open(output_file2,"w")
	dialouge_count = 0
	for line in content1:
		fh1.write(line)
		dialouge_count =+1
		if dialouge_count >= max_dialouge_count and max_dialouge_count != -1:
			break
	fh1.close()
	for line in content2:
		fh1.write(line)
		dialouge_count =+1
		if dialouge_count >= max_dialouge_count and max_dialouge_count != -1:
			break
	fh2.close()
	return output_file1, output_file2



def extract_dialouge_vocab(input_file1, input_file2, max_dialouge_count, output_file1, output_file2, vocab_file1, vocab_file2):
	output_file1, output_file2= dialouge_extract(input_file1, input_file2, max_dialouge_count, output_file1, output_file2)
	vocab_dict1 = get_vocab(output_file1)
	vocab_dict2 = get_vocab(output_file2)
	write_dict(vocab_file1, vocab_dict1, "key")
	write_dict(vocab_file2, vocab_dict2, "key")


def compare_chat_reply(output_file1, output_file2, num):
    valid_bool = True
    content1 = read_file_line_by_line(output_file1)
    content2 = read_file_line_by_line(output_file2)
    len1 = len(content1)
    len2 = len(content2)
    print(" Length of file \"%s\"- %s" % (output_file1, len1))
    print(" Length of file \"%s\"- %s" % (output_file2, len2))
    if(len1!=len2):
	print(" Length of file \" %s \" and \" %s \" not equal, difference: %s" % (output_file1, output_file2,(len1-len2)))
	valid_bool = False

    i = 0
    for i in range(num):
	print(" File - \"%s\"- %s" % (output_file1, content1[i]))
	print(" File - \"%s\"- %s" % (output_file2, content2[i]))
	print(" --------------------------------------------------------")
        i +=1
    return valid_bool


# writes input output file
def dialouge_seperator(filename):
    output_file = filename
    if filename[len(filename)-4:] == ".txt":
        output_file = filename[:len(filename)-4]
    output_file1 = output_file + "_1.txt"
    output_file2 = output_file + "_2.txt"

    p1 = 0
    fh1 = open(output_file1,"w")
    fh2 = open(output_file2,"w")
    for line in open(filename):
        if p1 == 0:
             fh1.write(line)
         p1 = 1
    else:
             fh2.write(line)
         p1 = 0
    fh1.close()
    fh2.close()



# writes input output file
def dialouge_seperator_cornell_movie(filename, symbol_seq, max_dialouge_count, output_file1, output_file2):
    output_file = filename
    if filename[len(filename)-4:] == ".txt":
        output_file = filename[:len(filename)-4]

    p1 = ""
    fh1 = open(output_file1,"w")
    fh2 = open(output_file2,"w")
    dialouge_count = 0  
    for line in reversed(list(open(filename))):
        line = extract_line_af(line, symbol_seq)
        if p1 == "":
            fh1.write(line)
            p1 = line
        elif p1 != "" and dialouge_count == 1:
            fh2.write(line)
            p1 = line
        else:
            fh1.write(p1)
            fh2.write(line)
            p1 = line
        dialouge_count +=1
        if dialouge_count >= max_dialouge_count and max_dialouge_count != -1:
            break
    fh1.close()
    fh2.close()
    return output_file1, output_file2




# open subtitle

# writes input output file
def dialouge_seperator_open_subtitle(filename, output_file1, output_file2, max_dialouge_count):
    output_file = filename
    #if filename[len(filename)-4:] == ".txt":
    #    output_file = filename[:len(filename)-4]

    #output_file1 = output_file + "_1.txt"
    #output_file2 = output_file + "_2.txt"
   
    p1 = ""
    fh1 = open(output_file1,"w")
    fh2 = open(output_file2,"w")
    i = 0
    dialouge_count = 0
    for line in open(filename):
        if i == 0:
            p1 = line
        else:
            if line!=p1:
                fh1.write(p1)
                fh2.write(line)
                p1 = line
                dialouge_count +=1
                i +=1   
        if dialouge_count >= max_dialouge_count and max_dialouge_count != -1:
            break
    fh1.close()
    fh2.close()
    return output_file1, output_file2


# movie subtitle

# writes input output file
def dialouge_seperator_movie_subtitle(filename, output_file1, output_file2, max_dialouge_count):
    p1 = ""
    fh1 = open(output_file1,"w")
    fh2 = open(output_file2,"w")
    i = 0
    dialouge_count = 0
    for line in open(filename):
    if i == 0:
       p1 = line
    else:
        if line != p1:
            fh1.write(p1)
            fh2.write(line)
            p1 = line
        dialouge_count +=1
    i +=1   
    if dialouge_count >= max_dialouge_count and max_dialouge_count != -1:
       break
    fh1.close()
    fh2.close()
    return output_file1, output_file2


filename = "corpus/extracted/open_subtitles.txt"
output_file1 = "processed_dialouge/open_subtitles/train.en"
output_file2 = "processed_dialouge/open_subtitles/train.vi"
vocab_file1 = "processed_dialouge/open_subtitles/vocab.en"
vocab_file2 = "processed_dialouge/open_subtitles/vocab.vi"
dialouge_count = 300
dialouge_count = -1

start = time.time()
output_file1, output_file2 = dialouge_seperator_open_subtitle(filename, "train.en", "train.vi", dialouge_count)
print(output_file1, output_file2)
vocab_dict1 = get_vocab(output_file1)
vocab_dict2 = get_vocab(output_file2)
write_dict("vocab.en", vocab_dict1, "key")
write_dict("vocab.vi", vocab_dict2, "key")
compare_chat_reply(output_file1, output_file2, 100)
end = time.time()
time_lib.elapsed_time(start, end)

'''
# cornell movie

filename = "corpus/extracted/movie_lines.txt"
output_file1 = "processed_dialouge/cornell_movie/train.en"
output_file2 = "processed_dialouge/cornell_movie/train.vi"
vocab_file1 = "processed_dialouge/cornell_movie/vocab.en"
vocab_file2 = "processed_dialouge/cornell_movie/vocab.vi"
#dialouge_count = 300
dialouge_count = -1
symbol_seq = '+++$+++ '

start = time.time()
output_file1, output_file2 = dialouge_seperator_cornell_movie(filename, symbol_seq, dialouge_count, output_file1, output_file2)
vocab_dict1 = get_vocab(output_file1)
vocab_dict2 = get_vocab(output_file2)
write_dict(vocab_file1, vocab_dict1, "key")
write_dict(vocab_file2, vocab_dict2, "key")
compare_chat_reply(output_file1, output_file2, 10)
end = time.time()
time_lib.elapsed_time(start, end)
'''
'''
filename = "corpus/extracted/movie_subtitles_en.txt"
output_file1 = "processed_dialouge/movie_subtitles/train.en"
output_file2 = "processed_dialouge/movie_subtitles/train.vi"
vocab_file1 = "processed_dialouge/movie_subtitles/vocab.en"
vocab_file2 = "processed_dialouge/movie_subtitles/vocab.vi"
#dialouge_count = 300
dialouge_count = -1


start = time.time()
output_file1, output_file2 = dialouge_seperator_movie_subtitle(filename, output_file1, output_file2, dialouge_count)
print(output_file1, output_file2)
vocab_dict1 = get_vocab(output_file1)
vocab_dict2 = get_vocab(output_file2)
write_dict(vocab_file1, vocab_dict1, "key")
write_dict(vocab_file2, vocab_dict2, "key")
compare_chat_reply(output_file1, output_file2, 10)
end = time.time()
time_lib.elapsed_time(start, end)

'''


