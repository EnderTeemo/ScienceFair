import serial
import csv
import sys
import datetime

num_cal_samples = 40

sum_x = 0
sum_y = 0
sum_z = 0

cal_x = 0
cal_y = 0
cal_z = 0

# Random number that you'll have to set yourself to make it activate the way you want
# SO basically higher number means harder to activate, smaller number means easier to activate
activation_distance = 100
# with serial.Serial('COM1', 19200, timeout=1) as serial_con:
	# x = serial_con.readline()

ser = serial.Serial('COM1')

# Cycle the serial connection
ser.close()
ser.open()
filename = raw_input('File name?')
for x in range(num_cal_samples):
	line = ser.readline()

	# [AccelerationX, AccelerationY, AccelerationZ, GyroX, GyroY, GyroZ]
	list_of_values = line.split()
	# print 'AccelerationX ',
	# print list_of_values[0],
	sum_x += int(list_of_values[0])
	sum_y += int(list_of_values[1])
	sum_z += int(list_of_values[2])
	print x+1

	# print 'GyroY ',
	# print list_of_values[4]
	# print line

cal_x = sum_x / num_cal_samples
cal_y = sum_y / num_cal_samples
cal_z = sum_z / num_cal_samples
print cal_x, cal_y, cal_z
with open(filename + '.csv', 'w+') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['CalibrationX', 'CalibrationY', 'CalibrationZ'])
	writer.writerow([cal_x, cal_y, cal_z])
	writer.writerow(['AccelerationX', 'AccelerationY', 'AccelerationZ', 'Time'])
	while True:
		line = ser.readline()
		time_now = datetime.datetime.now().time()
		list_of_values = line.split()
		print list_of_values[0:3]

		# Equations to check if out side of activatable threshold
		# The arm explanation kek
		
		bool_x = abs(int(list_of_values[0]) - cal_x) > activation_distance
		bool_y = abs(int(list_of_values[1]) - cal_y) > activation_distance
		bool_z = abs(int(list_of_values[2]) - cal_z) > activation_distance
		line_to_write = list_of_values[0:3]
		line_to_write.append(time_now)

		if bool_x or bool_y or bool_z:
			line_to_write.append('Activated')
			print '====== Activated ======'
		else:
			print 'It\'s casual'
		writer.writerow(line_to_write)