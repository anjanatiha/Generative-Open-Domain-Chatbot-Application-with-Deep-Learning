import time

def elapsed_time(start, end):
    hours, rem = divmod(end-start, 3600)
    minutes, seconds = divmod(rem, 60)
    print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))


def elapsed_time2(start, end):
    temp = end-start
    hours = temp//3600
    temp = temp - 3600*hours
    minutes = temp//60
    seconds = temp - 60*minutes
    print('%d:%d:%d' %(hours,minutes,seconds))


#print elapsed time in hh:mm:ss format
def format_time(start_time, end_time):
    elsapsed_time = end_time - start_time
    hr = int(elsapsed_time)//3600
    min_ = (int(elsapsed_time) - (hr * 3600))/60
    sec = int(elsapsed_time) - hr * 3600 - min_ * 60
    print("HH:Min:Sec > " + str(hr) +" hr " + str(min_) + " min "+ str(sec) + "sec")


def sleep(sec):
    time.sleep(sec) 

