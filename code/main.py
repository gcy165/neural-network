from mnist_loader import *
#from network import *
from network_gcy import *
import time

time_start = time.time()

# read the DataSet
training_data, validation_data, test_data = load_data_wrapper()
# set up a network
net = Network([784, 30, 10])
net.SGD(training_data, 30, 10, 0.1, lmbda = 5.0, test_data=test_data)

time_end = time.time()
print "Time: " + str(time_end-time_start) + "s"