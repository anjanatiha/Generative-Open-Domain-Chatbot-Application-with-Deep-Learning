import sys, os
import subprocess
import random
import re


#############
#input_file = "/home/anjanatiha/Downloads/project/Code/current_code/inout/output/nmt_model/my_infer_file.vi"
#output_file = "/home/anjanatiha/Downloads/project/Code/current_code/inout/output/nmt_model/output_infer"
#shell_script = './response.sh'

#######################################

cur_dir = os.path.dirname(os.getcwd())
#print("------------------------")
#print(cur_dir)
#print("------------------------")
input_file = cur_dir + "/current_code/inout/output/nmt_model/my_infer_file.vi"
output_file = cur_dir + "/current_code/inout/output/nmt_model/output_infer"
shell_script = './response.sh'


# converts text to lowercase
def to_lower(text):
	return text.lower()


# removes multiple puncs with single punc (list)
def remove_multi_punc_list(text, sym_list):
	for sym in sym_list:
		text = re.sub(r'\%s+' % sym, sym, text)
	return text


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


# write file
def write(filename, content):
	fh = open(filename,"w")
	fh.write(content)
	fh.close()

# reads file line by line/ splits by line
def read_file_lines(filename):             
    with open(filename, 'r') as content_file:
        content = content_file.readlines()
    return content


# delete one single directory
def delete_directory(dir_name):
	if(os.path.isdir(dir_name)):
		try:
			shutil.rmtree(dir_name)
		except OSError as e:
			if(e.errno != errno.EEXIST):
				raise
		pass 
		
#delete if file is empty
def delete_file(path):
	try:
		os.remove(path)
	except WindowsError:
		print("failed deleting: " + path)
		pass

def process_input_str(input_str):

	pattern_str1 = '[^a-zA-Z\'.,!?]'
	pattern_str2 = "([^a-zA-Z0-9\'])"
	substitute_str1 = " "
	add_str = " "
	
	sym_list = ['.',',','?','!',' ', '\'']

	input_str_temp = substitute_pattern(input_str, pattern_str1, substitute_str1)
	input_str_temp = remove_multi_punc_list(input_str_temp, sym_list)
	input_str_temp = add_pattern(input_str_temp, pattern_str2, add_str, before = 1, after = 1)
	input_str_temp = remove_multi_punc_list(input_str_temp, " ")
	input_str_temp = input_str_temp.lower()
	input_str_temp = input_str_temp.strip()
	
	return input_str_temp	


def get_response(input_str):
	selected_response_dict = {}
	input_str_temp = process_input_str(input_str) ###########aadd
	print("input_str_temp: ", input_str_temp)
	write(input_file, input_str_temp) ############add
	os.system("sh response.sh")
	response_list = read_file_lines(output_file)
	delete_file(output_file)

	random_num = random.randrange(0, len(response_list), 1)
	selected_response_dict[random_num] = 1

	selected_response = response_list[random_num]
	
	responses = ""
	for response in response_list:
		responses = responses + response + "\n"

	print(responses)
	print(selected_response)
	
	return selected_response, responses


