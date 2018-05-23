import re
import time
import time_lib
import codecs
import os, shutil
import random

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

# removes multiple puncs with single punc(basic)
def remove_multi_punc_basic(text):
	text = re.sub(r'\.+', '.', text) 
	text = re.sub(r',+', ',', text) 
	text = re.sub(r'\?+', '?', text) 
	text = re.sub(r' +', ' ', text) 
	return text

# removes multiple puncs with single punc
def remove_multi_punc(text, sym):
	text = re.sub(r'\%s+' % sym,sym,text)
	return text


# removes multiple puncs with single punc (list)
def remove_multi_punc_list(text, sym_list):
	for sym in sym_list:
		text = re.sub(r'\%s+' % sym, sym, text)
	return text


# add space before and after the punctuation
def add_space_punc(text):
	return re.sub("([^a-zA-Z0-9])", r' \1 ', text)


# add space before and after the punctuation
def add_space_punc_2(text):
	return re.sub("([^a-zA-Z0-9\'])", r' \1 ', text)


# remove all the characters except alphabetical
# removes special characters and numerical charcharters
def remove_non_alpha(text):
	return re.sub(r'[^a-zA-Z]', ' ', text)


# remove all the characters except alphabetical
# removes special characters and numerical charcharters
def remove_non_alpha_2(text):
	return re.sub(r'[^a-zA-Z\'.?]', ' ', text)




# substitute text pattern with replacement string
def substitute_pattern(text, patttern_str, replace_str):
	text = re.sub(r'%s' % patttern_str, replace_str, text)
	return text

# add text before or/and after pattern
def add_pattern(text, pattern_str, replace_str, before, after):
	if before == 1 and after == 0:
		text = re.sub(r'%s' % pattern_str, r'%s\1' % (replace_str), text)
	elif before == 0 and after == 1:
		text = re.sub(r'%s' % pattern_str, r'\1%s' % (replace_str), text)
	elif before == 1 and after == 1:
		text = re.sub(r'%s' % pattern_str, r'%s\1%s' % (replace_str, replace_str), text)

	return text



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
def dialouge_seperator(raw_dialogue_file_path, dialogue_file1, dialogue_file2):
	fh1 = open(dialogue_file1,"w")
	fh2 = open(dialogue_file2,"w")

	p1 = 0

	for line in open(raw_dialogue_file_path):
		if p1 == 0:
			fh1.write(line)
			p1 = 1

		else:
			fh2.write(line)
			p1 = 0

	fh1.close()
	fh2.close()


# preproceses dialouge cornell_movie
def dialouge_seperator_cornell_movie(raw_dialogue_file_path, dialogue_file1, dialogue_file2, symbol_seq, max_dialouge_count, max_len):
	print("dialouge_seperator_cornell_movie")

	fh1 = open(dialogue_file1,"w")
	fh2 = open(dialogue_file2,"w")

	total_count = 0
	dialouge_count = 0 
	dialouge_count_deleted = 0  
	
	p1 = ""
	p2 = ""

	prev_movie_id = ""
	prev_character = ""

	p1_pos = 0
	p2_pos = 0
	
	p = 0
	

	pattern_str1 = '[^a-zA-Z\'.,!?]'
	pattern_str2 = "([^a-zA-Z0-9\'])"
	substitute_str1 = " "
	add_str = " "
	
	sym_list = ['.',',','?','!',' ', '\'']
	
	for line in reversed(list(open(raw_dialogue_file_path))):

		line_temp = line 
		line_temp = extract_line_af(line_temp, symbol_seq)

		line_temp = substitute_pattern(line_temp, pattern_str1, substitute_str1)
		line_temp = remove_multi_punc_list(line_temp, sym_list)
		line_temp = add_pattern(line_temp, pattern_str2, add_str, before = 1, after = 1)
		line_temp = remove_multi_punc_list(line_temp, " ")

		line_temp = line_temp.decode('utf-8', 'ignore') 
		#line = line.encode().decode('utf-8', 'ignore')  
		line_temp = line_temp.lower()
		line_temp = line_temp.strip()
		line_temp = line_temp + "\n"

		temp = line.split("+++$+++")
		
		current_movie_id = temp[2].strip()
		current_character = temp[3].strip()

		if total_count == 0:
			p = 0


		if p == 0:
			p1 = line_temp
			p2 = ""
			p = 1
			p1_pos = total_count
			prev_movie_id = current_movie_id
			prev_character = current_character

		else:
			if prev_movie_id == current_movie_id and prev_character != current_character :
				p2 = line_temp
				fh1.write(p1)
				fh2.write(p2)
				p = 0
				p1 = p2
				p2 = ""
				p2_pos = total_count
				prev_movie_id = current_movie_id
				prev_character = current_character

				dialouge_count += 1
				diff = p2_pos - p1_pos
				if diff > 1:
					print(diff)

			elif prev_movie_id != current_movie_id:
				p = 1
				p1 = line_temp
				p2 = ""
				p1_pos = total_count
				prev_movie_id = current_movie_id
				prev_character = current_character
				dialouge_count_deleted +=1 

			elif prev_character == current_character and prev_movie_id == current_movie_id:
				p = 1
				p1 = line_temp
				p2 = ""
				p1_pos = total_count
				dialouge_count_deleted +=1 


		total_count +=1 




	print("dialouge_count: %d deleted_dialouge_count: %d " % (dialouge_count, dialouge_count_deleted))
	fh1.close()
	fh2.close()
	
	return dialogue_file1, dialogue_file2


# preproceses dialouge cornell_movie
def dialouge_seperator_cornell_movie2(raw_dialogue_file_path, dialogue_file1, dialogue_file2, symbol_seq, max_dialouge_count, max_len):
	print("dialouge_seperator_cornell_movie")

	fh1 = open(dialogue_file1,"w")
	fh2 = open(dialogue_file2,"w")

	dialouge_count = 0 
	dialouge_count_deleted = 0  
	p1 = ""
	p2 = ""
	
	current_movie_id = ""
	current_character = ""

	pattern_str1 = '[^a-zA-Z\'.,!?]'
	pattern_str2 = "([^a-zA-Z0-9\'])"
	substitute_str1 = " "
	add_str = " "
	
	sym_list = ['.',',','?','!',' ', '\'']
	
	for line in reversed(list(open(raw_dialogue_file_path))):

		line_original = line 
		line = extract_line_af(line, symbol_seq)

		line = substitute_pattern(line, pattern_str1, substitute_str1)
		line = remove_multi_punc_list(line, sym_list)
		line = add_pattern(line, pattern_str2, add_str, before = 1, after = 1)
		line = remove_multi_punc_list(line, " ")

		line = line.decode('utf-8', 'ignore') 
		#line = line.encode().decode('utf-8', 'ignore')  
		line = line.lower()
		line = line.strip()
		line = line + "\n"

		temp = line_original.split("+++$+++")
		
		if temp[2].strip() != current_movie_id.strip(): 
			current_movie_id = temp[2]
			current_character = temp[3]  ###############added
			p1 = line
			p2 = ""

		elif current_character == temp[3].strip(): ###############elif
			p1 = line.strip()
			p2 = ""

		else:
			current_character = temp[3]  

		if line.strip() == "":
			p1 = ""
			p2 = "" ##########added
			current_movie_id = "" ###############added
			current_character = ""  ###############added
		else:
			if p1.strip() == "":
				p1 = line.strip()
				p2 = ""
				current_movie_id = temp[2] ###############added
				current_character = temp[3]  ###############added
			else:
				if len(p1.strip().split(" ")) > max_len  and max_len !=-1: 
					if len(line.strip().split(" ")) > max_len:
						p1 = ""
						p2 = ""
						current_movie_id = "" ###############added
						current_character = ""  ###############added
					else:
						p1 = line.strip()
						p2 = ""
						current_movie_id = temp[2] ###############added
						current_character = temp[3]  ###############added

				elif len(line.strip().split(" ")) > max_len and max_len != -1: 
						p1 = ""
						p2 = ""
						current_movie_id = "" ###############added
						current_character = ""  ###############added

				else:
					p2 = line
					fh1.write(p1)
					fh2.write(line)
					p1 = line
					p2 = ""
					current_movie_id = temp[2] ###############added
					current_character = temp[3]  ###############added

					dialouge_count +=1
	
					if dialouge_count >= max_dialouge_count and max_dialouge_count != -1:
						
						break

	print("dialouge_count: ", dialouge_count)
	fh1.close()
	fh2.close()
	
	return dialogue_file1, dialogue_file2


# open subtitle

# writes input output file
def dialouge_seperator_open_subtitle(raw_dialogue_file_path, dialogue_file1, dialogue_file2, max_dialouge_count):
	print("dialouge_seperator_open_subtitle")
   
	p1 = ""
	dialouge_count = 0

	fh1 = open(dialogue_file1,"w")
	fh2 = open(dialogue_file2,"w")

	for line in open(raw_dialogue_file_path):
		line = add_space_punc(line)
		line = remove_multi_space(line)
		line = line.decode('utf-8', 'ignore')
		#line = line.strip()
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
	
	return dialogue_file1, dialogue_file2


# movie subtitle

# writes input output file
def dialouge_seperator_movie_subtitle(raw_dialogue_file_path, dialogue_file1, dialogue_file2, max_dialouge_count):
	print("dialouge_seperator_movie_subtitle")

	dialouge_count = 0
	p1 = ""

	fh1 = open(dialogue_file1,"w")
	fh2 = open(dialogue_file2,"w")

	for line in open(raw_dialogue_file_path):
		line = add_space_punc(line)
		line = remove_multi_space(line)
		line = line.decode('utf-8', 'ignore')
		#line = line.strip()
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
	
	return dialogue_file1, dialogue_file2



def dialouge_extract(input_file1, input_file2, max_dialouge_count, train_file1, train_file2):
	content1 = read_file_line_by_line(dialogue_file1)
	content2 = read_file_line_by_line(dialogue_file2)
	
	fh1 = open(train_file1,"w")
	fh2 = open(train_file2,"w")
	
	dialouge_count = 0
	
	for line in content1:
		fh1.write(line)
		dialouge_count =+1
	
		if dialouge_count >= max_dialouge_count and max_dialouge_count != -1:
			break
	
	fh1.close()

	dialouge_count = 0
	
	for line in content2:
		fh2.write(line)
		dialouge_count =+1
	
		if dialouge_count >= max_dialouge_count and max_dialouge_count != -1:
			break
	
	fh2.close()

def random_generator(start, end, count, step):
	random_num_dict = {} 

	for i in range(start, start+count):
		random_num = random.randrange(start, end)
		
		if random_num not in random_num_dict:
			random_num_dict[random_num] = random_num
		else:
			if i > 0:
				i = i - 1

	return random_num_dict




def compare_chat_reply(dialogue_file1, dialogue_file2, compare_count, type_rand):
	valid_bool = True
	
	content1 = read_file_line_by_line(dialogue_file1)
	content2 = read_file_line_by_line(dialogue_file2)
	
	len1 = len(content1)
	len2 = len(content2)
	
	print("\n\n Length of file \"%s\"- %s" % (dialogue_file1, len1))
	print(" Length of file \"%s\"- %s\n\n" % (dialogue_file2, len2))
	
	if(len1!=len2):
		print(" Length of file \" %s \" and \" %s \" not equal, difference: %s" % (dialogue_file1, dialogue_file2,(len1-len2)))
		valid_bool = False

	if type_rand == "": 
		i = 0
		for i in range(compare_count):
			#print(" File - \"%s\"- %s" % (dialogue_file1, content1[i]))
			#print(" File - \"%s\"- %s" % (dialogue_file2, content2[i]))

			print(" Person 1 : %s" % (content1[i]))
			print(" Person 2 : %s" % (content2[i]))
			
			print(" --------------------------------------------------------")
			i +=1
	else:
		random_num_dict = random_generator(0, len1, compare_count, -1)
		for key in random_num_dict:
			#print(" Person 1 (File - \"%s\")- %s)" % (dialogue_file1, content1[key]))
			#print(" Person 2 (File - \"%s\")- %s" % (dialogue_file2, content2[key]))

			print(" Person 1 : %s" % (content1[key]))
			print(" Person 2 : %s" % (content2[key]))
			print(" --------------------------------------------------------")
	
	return valid_bool


def delete_all_file_dir(dir_path, type_d):
	print("Deleting old preprocessed files")
	folder = dir_path
	for the_file in os.listdir(folder):
		file_path = os.path.join(folder, the_file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
			if type_d == "sub_inc":
				if os.path.isdir(file_path): 
					shutil.rmtree(file_path)
		except Exception as e:
			print(e)




def file_dir_name_fix(parent_dir, extracted_dir, pre_processed_dir, input_data_dir, movie_dir, dialogue_file1, dialogue_file2, train_file1, train_file2, test_file1, test_file2, dev_file1, dev_file2, vocab_file1, vocab_file2):
	print("Shaping file paths")
	pre_processed_dir = parent_dir + "/" + pre_processed_dir + "/" + movie_dir
	raw_dialogue_file_path = parent_dir + "/" + extracted_dir + "/" + movie_dir + ".txt"

	dialogue_file1 = pre_processed_dir + "/" + dialogue_file1
	dialogue_file2 = pre_processed_dir + "/" + dialogue_file2
	
	input_data_dir_path = parent_dir+ "/" + input_data_dir + "/" + movie_dir
	
	train_file1 = input_data_dir_path + "/" + train_file1
	train_file2 = input_data_dir_path + "/" + train_file2
	test_file1 = input_data_dir_path + "/" + test_file1
	test_file2 = input_data_dir_path + "/" + test_file2
	dev_file1 = input_data_dir_path + "/" + dev_file1
	dev_file2 = input_data_dir_path + "/" + dev_file2	
	vocab_file1 = input_data_dir_path + "/" + vocab_file1
	vocab_file2 = input_data_dir_path + "/" + vocab_file2

	return pre_processed_dir, raw_dialogue_file_path, dialogue_file1, dialogue_file2, train_file1, train_file2, test_file1, test_file2, dev_file1, dev_file2, vocab_file1, vocab_file2



def train_test_split(dialogue_file1, dialogue_file2, max_dialouge_count_train_test, train_percentile, train_file1, train_file2, test_file1, test_file2, dev_file1, dev_file2, max_test_dev_count):
	print("train_test_split")
	content1 = read_file_line_by_line(dialogue_file1)
	content2 = read_file_line_by_line(dialogue_file2)

	if len(content1) != len(content2):
		print("Two files dont have same length")

	if max_dialouge_count_train_test == -1:
		max_dialouge_count_train_test = len(content1)

	train_file_h1 = open(train_file1,"w")
	train_file_h2 = open(train_file2,"w")
	test_file_h1 = open(test_file1,"w")
	test_file_h2 = open(test_file2,"w")
	dev_file_h1 = open(dev_file1,"w")
	dev_file_h2 = open(dev_file2,"w")

	train_src_count = 0
	test_src_count = 0
	dev_src_count = 0
	train_target_count = 0
	test_target_count = 0
	dev_target_count = 0



	if max_test_dev_count == -1:
		train_end = int((max_dialouge_count_train_test*(float(train_percentile)/100)) - 1)
		test_end =  int(train_end + ((max_dialouge_count_train_test - train_end)/2))

	else:
		train_end = int(max_dialouge_count_train_test - 2*max_test_dev_count)
		test_end =  int(train_end + max_test_dev_count-1)
	

	dialouge_count = 0
	
	for line in content1:
		if dialouge_count <= train_end:
			train_file_h1.write(line)
			train_src_count += 1
		elif dialouge_count >= train_end and dialouge_count <= test_end:
			test_file_h1.write(line)
			test_src_count += 1
		else:
			dev_file_h1.write(line)
			dev_src_count += 1

		if dialouge_count >= max_dialouge_count_train_test and max_dialouge_count_train_test != -1:
			break
		dialouge_count +=1
	
	train_file_h1.close()
	test_file_h1.close()
	dev_file_h1.close()
	
	dialouge_count = 0

	for line in content2:
		if dialouge_count <= train_end:
			train_file_h2.write(line)
			train_target_count += 1
		elif dialouge_count >= train_end and dialouge_count <= test_end:
			test_file_h2.write(line)
			test_target_count += 1
		else:
			dev_file_h2.write(line)
			dev_target_count += 1

		if dialouge_count >= max_dialouge_count_train_test and max_dialouge_count_train_test != -1:
			break
		dialouge_count +=1

	print("train_src_count", train_src_count)
	print("test_src_count", test_src_count)
	print("dev_src_count", dev_src_count)
	print("train_target_count", train_target_count)
	print("test_target_count", test_target_count)
	print("dev_target_count", dev_target_count)
	
	train_file_h2.close()
	test_file_h2.close()
	dev_file_h2.close()


	return train_file1, train_file2, test_file1, test_file2, dev_file1, dev_file2



def train_test_split_seq2_seq(dialogue_file1, dialogue_file2, max_dialouge_count_train_test, train_percentile, train_file1, train_file2, test_file1, test_file2, max_test_dev_count):
	print("train_test_split")
	content1 = read_file_line_by_line(dialogue_file1)
	content2 = read_file_line_by_line(dialogue_file2)

	if len(content1) != len(content2):
		print("Two files dont have same length")

	if max_dialouge_count_train_test == -1:
		max_dialouge_count_train_test = len(content1)

	train_file_h1 = open(train_file1,"w")
	train_file_h2 = open(train_file2,"w")
	test_file_h1 = open(test_file1,"w")
	test_file_h2 = open(test_file2,"w")

	train_src_count = 0
	test_src_count = 0
	train_target_count = 0
	test_target_count = 0


	if max_test_dev_count == -1:
		train_end = int((max_dialouge_count_train_test*(float(train_percentile)/100)) - 1)

	else:
		train_end = int(max_dialouge_count_train_test - max_test_dev_count)
	

	dialouge_count = 0
	
	for line in content1:
		if dialouge_count <= train_end:
			train_file_h1.write(line)
			train_src_count += 1
		elif dialouge_count >= train_end:
			test_file_h1.write(line)
			test_src_count += 1

		if dialouge_count >= max_dialouge_count_train_test and max_dialouge_count_train_test != -1:
			break
		dialouge_count +=1
	
	train_file_h1.close()
	test_file_h1.close()
	
	dialouge_count = 0

	for line in content2:
		if dialouge_count <= train_end:
			train_file_h2.write(line)
			train_target_count += 1
		elif dialouge_count >= train_end:
			test_file_h2.write(line)
			test_target_count += 1

		if dialouge_count >= max_dialouge_count_train_test and max_dialouge_count_train_test != -1:
			break
		dialouge_count +=1

	print("train_src_count", train_src_count)
	print("test_src_count", test_src_count)
	print("train_target_count", train_target_count)
	print("test_target_count", test_target_count)
	
	train_file_h2.close()
	test_file_h2.close()


	return train_file1, train_file2, test_file1, test_file2, dev_file1, dev_file2



def pre_process_dialouge(raw_dialogue_file_path, pre_processed_dir, movie_dir_name, dialogue_file1, dialogue_file2, train_file1, train_file2, test_file1, test_file2, dev_file1, dev_file2, vocab_file1, vocab_file2, max_dialouge_count, max_dialouge_count_train_test, train_percentile, compare_count, symbol_seq, type_d, max_len, type_rand, max_test_dev_count):
	print("Extracting file")

	start = time.time()
	
	delete_all_file_dir(pre_processed_dir, type_d)
	
	if movie_dir_name == cornell_movie_dir:
		dialogue_file1, dialogue_file2 = dialouge_seperator_cornell_movie(raw_dialogue_file_path, dialogue_file1, dialogue_file2, symbol_seq, max_dialouge_count, max_len)
	elif movie_dir_name == open_subtitles_dir:
		dialogue_file1, dialogue_file2 = dialouge_seperator_open_subtitle(raw_dialogue_file_path, dialogue_file1, dialogue_file2, max_dialouge_count)
	elif movie_dir_name == movie_subtitles_dir:
		dialogue_file1, dialogue_file2 = dialouge_seperator_movie_subtitle(raw_dialogue_file_path, dialogue_file1, dialogue_file2, max_dialouge_count)
	else:
		print("directory match not found")
		return

	#print(dialogue_file1, dialogue_file2)

	# gnmt model
	train_file1, train_file2, test_file1, test_file2, dev_file1, dev_file2 = train_test_split(dialogue_file1, dialogue_file2, max_dialouge_count_train_test, train_percentile, train_file1, train_file2, test_file1, test_file2, dev_file1, dev_file2, max_test_dev_count)	

	

	'''
	vocab_dict1 = get_vocab(train_file1)
	vocab_dict2 = get_vocab(train_file2)

	write_dict(vocab_file1, vocab_dict1, "key")
	write_dict(vocab_file2, vocab_dict2, "key")
    '''

	compare_chat_reply(dialogue_file1, dialogue_file2, compare_count, type_rand)



	end = time.time()
	time_lib.elapsed_time(start, end)



def pre_process_dialouge_seq_2_seq(raw_dialogue_file_path, pre_processed_dir, movie_dir_name, dialogue_file1, dialogue_file2, train_file1, train_file2, test_file1, test_file2, max_dialouge_count, max_dialouge_count_train_test, train_percentile, compare_count, symbol_seq, type_d, max_len, type_rand, max_test_dev_count):
	print("Extracting file")

	start = time.time()
	
	delete_all_file_dir(pre_processed_dir, type_d)
	
	if movie_dir_name == cornell_movie_dir:
		dialogue_file1, dialogue_file2 = dialouge_seperator_cornell_movie(raw_dialogue_file_path, dialogue_file1, dialogue_file2, symbol_seq, max_dialouge_count, max_len)
	elif movie_dir_name == open_subtitles_dir:
		dialogue_file1, dialogue_file2 = dialouge_seperator_open_subtitle(raw_dialogue_file_path, dialogue_file1, dialogue_file2, max_dialouge_count)
	elif movie_dir_name == movie_subtitles_dir:
		dialogue_file1, dialogue_file2 = dialouge_seperator_movie_subtitle(raw_dialogue_file_path, dialogue_file1, dialogue_file2, max_dialouge_count)
	else:
		print("directory match not found")
		return

	#print(dialogue_file1, dialogue_file2)

	# gnmt model
	#train_file1, train_file2, test_file1, test_file2, dev_file1, dev_file2 = train_test_split(dialogue_file1, dialogue_file2, max_dialouge_count_train_test, train_percentile, train_file1, train_file2, test_file1, test_file2, dev_file1, dev_file2, max_test_dev_count)
	
	train_file1, train_file2, test_file1, test_file2, dev_file1, dev_file2 = train_test_split_seq2_seq(dialogue_file1, dialogue_file2, max_dialouge_count_train_test, train_percentile, train_file1, train_file2, test_file1, test_file2, max_test_dev_count)
		

	compare_chat_reply(dialogue_file1, dialogue_file2, compare_count, type_rand)



	end = time.time()
	time_lib.elapsed_time(start, end)


parent_dir = "corpus"
extracted_dir = "extracted"
pre_processed_dir = "pre_processed"
input_data_dir = "input_data"

dialogue_file1 = "train_test.en"
dialogue_file2 = "train_test.vi"

train_file1 = "train.en"
train_file2 = "train.vi"

tst2012_en = "tst2012.en"
tst2012_vi = "tst2012.vi"
tst2013_en = "tst2013.en"
tst2013_vi = "tst2013.vi"

test_file1 = tst2012_en
test_file2 = tst2012_vi

dev_file1 = tst2013_en
dev_file2 = tst2013_vi

vocab_file1 = "vocab.en"
vocab_file2 = "vocab.vi"



#######################
#seq2seq
train_enc = "train.enc"
train_dec = "train.dec"

test_enc = "test.enc"
test_dec = "test.dec"



cornell_movie_dir = "cornell_movie"
open_subtitles_dir = "open_subtitles"
movie_subtitles_dir = "movie_subtitles"


max_dialouge_count = -1
#max_dialouge_count = 5000
max_dialouge_count_train_test = -1
type_d = "sub_inc"
symbol_seq = '+++$+++ '


tst2012_size = 3000
tst2013_size = 3000

max_test_dev_count = tst2012_size


train_percentile = 97
#train_percentile = 75

# max len of sentence
#max_len = 100
max_len = -1

# print compare  
type_rand = "rand"
type_rand = ""
compare_count = 5

movie_dir = cornell_movie_dir
_pre_processed_dir, _raw_dialogue_file_path, _dialogue_file1, _dialogue_file2, _train_file1, _train_file2, _test_file1, _test_file2, _dev_file1, _dev_file2, _vocab_file1, _vocab_file2 = file_dir_name_fix(parent_dir, extracted_dir, pre_processed_dir, input_data_dir, movie_dir, dialogue_file1, dialogue_file2, train_file1, train_file2, test_file1, test_file2, dev_file1, dev_file2, vocab_file1, vocab_file2)
pre_process_dialouge(_raw_dialogue_file_path, _pre_processed_dir, movie_dir, _dialogue_file1, _dialogue_file2, _train_file1, _train_file2, _test_file1, _test_file2, _dev_file1, _dev_file2, _vocab_file1, _vocab_file2, max_dialouge_count, max_dialouge_count_train_test, train_percentile, compare_count, symbol_seq, type_d, max_len, type_rand, max_test_dev_count)

#pre_process_dialouge_seq_2_seq(_raw_dialogue_file_path, _pre_processed_dir, movie_dir, _dialogue_file1, _dialogue_file2, train_enc, train_dec, test_enc, test_dec, max_dialouge_count, max_dialouge_count_train_test, train_percentile, compare_count, symbol_seq, type_d, max_len, type_rand, max_test_dev_count)


'''
movie_dir = open_subtitles_dir
_pre_processed_dir, _raw_dialogue_file_path, _dialogue_file1, _dialogue_file2, _train_file1, _train_file2, _test_file1, _test_file2, _dev_file1, _dev_file2, _vocab_file1, _vocab_file2 = file_dir_name_fix(parent_dir, extracted_dir, pre_processed_dir, input_data_dir, movie_dir, dialogue_file1, dialogue_file2, train_file1, train_file2, test_file1, test_file2, dev_file1, dev_file2, vocab_file1, vocab_file2)
pre_process_dialouge(_raw_dialogue_file_path, _pre_processed_dir, movie_dir, _dialogue_file1, _dialogue_file2, _train_file1, _train_file2, _test_file1, _test_file2, _dev_file1, _dev_file2, _vocab_file1, _vocab_file2, max_dialouge_count, max_dialouge_count_train_test, train_percentile, compare_count, symbol_seq, type_d)

movie_dir = movie_subtitles_dir
_pre_processed_dir, _raw_dialogue_file_path, _dialogue_file1, _dialogue_file2, _train_file1, _train_file2, _test_file1, _test_file2, _dev_file1, _dev_file2, _vocab_file1, _vocab_file2 = file_dir_name_fix(parent_dir, extracted_dir, pre_processed_dir, input_data_dir, movie_dir, dialogue_file1, dialogue_file2, train_file1, train_file2, test_file1, test_file2, dev_file1, dev_file2, vocab_file1, vocab_file2)
pre_process_dialouge(_raw_dialogue_file_path, _pre_processed_dir, movie_dir, _dialogue_file1, _dialogue_file2, _train_file1, _train_file2, _test_file1, _test_file2, _dev_file1, _dev_file2, _vocab_file1, _vocab_file2, max_dialouge_count, max_dialouge_count_train_test, train_percentile, compare_count, symbol_seq, type_d)
'''
