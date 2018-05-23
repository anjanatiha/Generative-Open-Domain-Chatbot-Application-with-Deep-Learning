import os, errno
import math
import operator 
import collections
from collections import OrderedDict
from collections import deque
import queue
import shutil
import pickle
import numpy as np
import copy


#load object from pickle file
def load_obj(name):
    file = open(name,'rb')
    object_file = pickle.load(file)
    file.close()
    
    return object_file
  

    
#load queue object from pickle file
def load_obj_no_sort_w(filename):
    link_queue = queue.Queue()
    link_list =[]
    
    if (os.path.isfile(filename)):
        file = open(filename,'rb')
        link_list = pickle.load(file)
        file.close()
        
        for link in link_list:
            link_queue.put(link)
        return link_queue
    
    else:
        print("no file found")
        return


#save object     
def save_obj_without_sort(obj, name):
    pickle.dump( obj, open( name + ".p", "wb" ) )


# save object in pickle
def load_obj_no_sort(name):
    file = open(name,'rb')
    object_file = pickle.load(file)
    file.close()
    
    return object_file


# save object in pickle
def save_obj_no_sort(obj, name):
    filename = name + ".p"
    
    if (os.path.isfile(filename)):
        os.remove(filename)
        
    pickle.dump( obj, open( filename, "wb" ) )
       

# save object in pickle
def save_obj(obj, name, key_or_val, order):
    filename = name + ".p"
    
    if(key_or_val == "key" and order == "auto"):
        sorted_x = sorted(obj.items(), key=operator.itemgetter(0))
    elif(key_or_val == "key" and order == "reverse"):
        sorted_x = sorted(obj.items(), key=operator.itemgetter(0), reverse=True)
    elif(key_or_val == "value" and order == "auto"):
        sorted_x = sorted(obj.items(), key=operator.itemgetter(1))
    elif(key_or_val == "value" and order == "reverse"):
        sorted_x = sorted(obj.items(), key=operator.itemgetter(1), reverse=True)
    if (os.path.isfile(filename)):
        os.remove(filename)
        
    pickle.dump( obj, open( filename, "wb" ) )


    
#save queue in pickle
def save_queue_no_sort_w(queue1, filename):
    link_list = []
    
    new_queue = queue.Queue()
    new_queue.queue = copy.deepcopy(queue1.queue)
    if (os.path.isfile(filename)):
        os.remove(filename)
        
    while(new_queue.empty() == False):
        link_list.append(new_queue.get())
        
    filename = filename + ".p"
    
    pickle.dump( link_list, open( filename, "wb" ) )

    

 
    

