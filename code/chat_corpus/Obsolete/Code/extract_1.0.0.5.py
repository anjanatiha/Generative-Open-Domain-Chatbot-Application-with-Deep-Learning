import re
import time
import time_lib
import codecs
import os, shutil
#import sys
#reload(sys)
#sys.setdefaultencoding('UTF-8')


# read file line by line/ splits by line
def read_file_line_by_line(filename):   
    with open(filename, "r") as content_file:
        content = content_file.readlines()
    return content

# reads file in reverse
def read_file_line_by_line_reverse(filename):
    for line in reversed(list(open(filename))):
        print(line)


# write file
def write(filename, content):
    fh = open(filename,"w")
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


# extract sequence after last occurance
def extract_line_af(line, symbol_seq):
    return line.rsplit(symbol_seq)[-1]

# extract sequence after last occurance for multiple lines
def extract_line_af_all(content, symbol_seq):
    for line in content:
    	line_ex = extract_line_af(line, symbol_seq)
    	print(line_ex)


# reads in reverse and extract sequence after last occurance for multiple lines
def extract_line_af_file(filename, symbol_seq):
    for line in reversed(list(open(filename))):
    	line_ex = extract_line_af(line, symbol_seq)
    	print(line_ex)


# get vocubulory
def get_vocab(filename):
    word_vocab = {}

    content = read_file_line_by_line(filename)

    print(" Getting vocabulory from file: \"%s\" ........."%filename)

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





# writes dictionary 
def write_dict_line(filename, vocab_dict, type_p):
    fh = open(output_file,"w")
    
    output_file = filename
    buffer_str = ""
    
    print("Writing dictionary to file: \"%s\" (%s) ........." % (filename, type_p))
    print(" Vocab length: %s"% len(vocab_dict))

    if type_p == "key":
        i = 0

        for word in vocab_dict:
            fh.write(word)
    else:
        i = 0
        for word in vocab_dict: 
            buffer_str = word + " , "+ vocab_dict[word]
            fh.write(buffer_str)

    fh.close()

    return output_file

# writes dictionary 
def write_dict(filename, vocab_dict, type_p):

    output_file = filename

    fh = open(output_file,"w")

    buffer_str = ""
    
    print("Writing dictionary to file: \"%s\" (%s) ........." % (filename, type_p))
    print(" Vocab length: %s"% len(vocab_dict))
    
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

# writes input output file
def dialouge_seperator(filename):
    output_file = filename

    if filename[len(filename)-4:] == ".txt":
        output_file = filename[:len(filename)-4]

    output_file1 = output_file + "_1.txt"
    output_file2 = output_file + "_2.txt"

    fh1 = open(output_file1,"w")
    fh2 = open(output_file2,"w")
    p1 = 0

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

    fh1 = open(output_file1,"w")
    fh2 = open(output_file2,"w")

    dialouge_count = 0  
    p1 = ""
    
    for line in reversed(list(open(filename))):
        line = extract_line_af(line, symbol_seq)
        line = add_space_punc(line)
        line = remove_multi_space(line)

        line = line.decode('utf-8', 'ignore')
    
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
    print("dialouge_seperator_open_subtitle")
   
    p1 = ""
    dialouge_count = 0

    fh1 = open(output_file1,"w")
    fh2 = open(output_file2,"w")

    for line in open(filename):
        line = add_space_punc(line)
        line = remove_multi_space(line)
        line = line.decode('utf-8', 'ignore')
        if dialouge_count == 0:
            p1 = line
        else:
            if line != p1:
                fh1.write(p1)
                fh2.write(line)
                p1 = line

        dialouge_count +=1

        if dialouge_count >= max_dialouge_count and max_dialouge_count != -1:
            break
    
    fh1.close()
    fh2.close()
    
    return output_file1, output_file2


# movie subtitle

# writes input output file
def dialouge_seperator_movie_subtitle(filename, output_file1, output_file2, max_dialouge_count):
    print("dialouge_seperator_movie_subtitle")

    dialouge_count = 0
    p1 = ""

    fh1 = open(output_file1,"w")
    fh2 = open(output_file2,"w")

    for line in open(filename):
        line = add_space_punc(line)
        line = remove_multi_space(line)
        line = line.decode('utf-8', 'ignore')
        if dialouge_count == 0:
            p1 = line
        else:
            if line != p1:
                fh1.write(p1)
                fh2.write(line)
                p1 = line

        dialouge_count +=1

        if dialouge_count >= max_dialouge_count and max_dialouge_count != -1:
            break
    
    fh1.close()
    fh2.close()
    
    return output_file1, output_file2



def dialouge_extract(input_file1, input_file2, max_dialouge_count, output_file1, output_file2):
    content1 = read_file_line_by_line(input_file1)
    content2 = read_file_line_by_line(input_file2)
    
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


def delete_all_file_dir(dir_path, type_d):
	folder = dir_path
	for the_file in os.listdir(folder):
	    file_path = os.path.join(folder, the_file)
	    try:
	        if os.path.isfile(file_path):
	            os.unlink(file_path)
	        if type_d == "inc_sub":
	        	os.path.isdir(file_path): shutil.rmtree(file_path)
	    except Exception as e:
	        print(e)




# cornell movie
out_dir_path = "corpus/pre_processed/cornell_movie"
filename = "corpus/extracted/movie_lines.txt"
output_file1 = "corpus/pre_processed/cornell_movie/train.en"
output_file2 = "corpus/pre_processed/cornell_movie/train.vi"
vocab_file1 = "corpus/pre_processed/cornell_movie/vocab.en"
vocab_file2 = "corpus/pre_processed/cornell_movie/vocab.vi"

#dialouge_count = 300
dialouge_count = -1
symbol_seq = '+++$+++ '
type_d = "sub_inc"

start = time.time()

delete_all_file_dir(out_dir_path, type_d)

output_file1, output_file2 = dialouge_seperator_cornell_movie(filename, symbol_seq, dialouge_count, output_file1, output_file2)

vocab_dict1 = get_vocab(output_file1)
vocab_dict2 = get_vocab(output_file2)

write_dict(vocab_file1, vocab_dict1, "key")
write_dict(vocab_file2, vocab_dict2, "key")

compare_chat_reply(output_file1, output_file2, 10)

end = time.time()
time_lib.elapsed_time(start, end)

parent_dir = "corpus"
extracted_dir = "extracted"
pre_processed_dir = "pre_processed"
cornell_movie_dir = "cornell_movie"
open_subtitles_dir = "open_subtitles"
movie_subtitles_dir = "movie_subtitles"
output_file1 = "train.en"
output_file2 = "train.vi"
vocab_file1 = "vocab.en"
vocab_file2 = "vocab.vi"

dialouge_count = -1
type_d = "sub_inc"

def file_dir_name_fix(parent_dir, extracted_dir, pre_processed_dir, movie_dir, output_file1, output_file2, vocab_file1, vocab_file2):
	out_dir_path = parent_dir+ "/" + pre_processed + "/" + movie_dir
	input_file_path = parent_dir+ "/" + extracted_dir + "/" + movie_dir + ".txt"
	output_file1 = parent_dir+ "/" + pre_processed + "/" + movie_dir + output_file1
	output_file2 = parent_dir+ "/" + pre_processed + "/" + movie_dir + output_file2
	vocab_file1 = parent_dir+ "/" + pre_processed + "/" + movie_dir + vocab_file1
	vocab_file2 = parent_dir+ "/" + pre_processed + "/" + movie_dir + vocab_file2

	return out_dir_path, input_file_path, output_file1, output_file2, vocab_file1, vocab_file2


out_dir_path, input_file_path, output_file1, output_file2, vocab_file1, vocab_file2 = file_dir_name_fix(parent_dir, extracted_dir, pre_processed_dir, movie_dir, output_file1, output_file2, vocab_file1, vocab_file2)

def all(out_dir_path, input_file_path, output_file1, output_file2, vocab_file1, vocab_file2, dialouge_count, type_d):

	start = time.time()
	delete_all_file_dir(out_dir_path, type_d)

	output_file1, output_file2 = dialouge_seperator_open_subtitle(filename, output_file1, output_file2, dialouge_count)
	print(output_file1, output_file2)

	vocab_dict1 = get_vocab(output_file1)
	vocab_dict2 = get_vocab(output_file2)

	write_dict(vocab_file1, vocab_dict1, "key")
	write_dict(vocab_file2, vocab_dict2, "key")

	compare_chat_reply(output_file1, output_file2, 100)

	end = time.time()
	time_lib.elapsed_time(start, end)





# open subtitle
out_dir_path = "corpus/pre_processed/open_subtitles"
filename = "corpus/extracted/open_subtitles.txt"
output_file1 = "corpus/pre_processed/open_subtitles/train.en"
output_file2 = "corpus/pre_processed/open_subtitles/train.vi"
vocab_file1 = "corpus/pre_processed/open_subtitles/vocab.en"
vocab_file2 = "corpus/pre_processed/open_subtitles/vocab.vi"
#dialouge_count = 300
dialouge_count = -1
type_d = "sub_inc"




# movie subtitle
out_dir_path = "corpus/pre_processed/movie_subtitles"
filename = "corpus/extracted/movie_subtitles_en.txt"
output_file1 = "corpus/pre_processed/movie_subtitles/train.en"
output_file2 = "corpus/pre_processed/movie_subtitles/train.vi"
vocab_file1 = "corpus/pre_processed/movie_subtitles/vocab.en"
vocab_file2 = "corpus/pre_processed/movie_subtitles/vocab.vi"

#dialouge_count = 300
dialouge_count = -1
type_d = "sub_inc"


start = time.time()

delete_all_file_dir(out_dir_path, type_d)

output_file1, output_file2 = dialouge_seperator_movie_subtitle(filename, output_file1, output_file2, dialouge_count)

print(output_file1, output_file2)

vocab_dict1 = get_vocab(output_file1)
vocab_dict2 = get_vocab(output_file2)

write_dict(vocab_file1, vocab_dict1, "key")
write_dict(vocab_file2, vocab_dict2, "key")

compare_chat_reply(output_file1, output_file2, 10)

end = time.time()
time_lib.elapsed_time(start, end)



