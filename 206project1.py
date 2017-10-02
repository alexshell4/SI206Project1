import os
import filecmp

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys will come from the first row in the data.

#Note: The column headings will not change from the
#test cases below, but the the data itself will
#change (contents and size) in the different test
#cases.

	#Your code here:
	file = open(file, 'r')
	output_list = list()
	for line in file.readlines()[1:]:
		dictionary = dict()
		line = line.split(',')
		dictionary['First'] = line[0]
		dictionary['Last'] = line[1]
		dictionary['Email'] = line[2]
		dictionary['Class'] = line[3]
		dictionary['DOB'] = line[4].strip()
		output_list.append(dictionary)
	return output_list


#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	sorted_data = sorted(data,key = lambda x:x[col])
	return sorted_data[0]['First']+' '+sorted_data[0]['Last']


#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	fres = 0
	soph = 0
	jun = 0
	sen = 0
	for person in data:
		if person['Class'] == 'Freshman':
			fres += 1
		if person['Class'] == 'Sophomore':
			soph += 1
		if person['Class'] == 'Junior':
			jun += 1
		if person['Class'] == 'Senior':
			sen += 1
	size_list = list()
	size_list.append(('Freshman', fres))
	size_list.append(('Sophomore', soph))
	size_list.append(('Junior', jun))
	size_list.append(('Senior', sen))
	return sorted(size_list, key = lambda x: x[1], reverse = True)


# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	dob_count = dict()
	for student in a:
		day = student['DOB'].split('/')[1]
		dob_count[day] = dob_count.get(day, 0) + 1
	return int(sorted([(k,v) for k,v in dob_count.items()], key = lambda x: x[1], reverse = True)[0][0])


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	total_age = 0
	for student in a:
		year = student['DOB'][-4:]
		age = 2017 - int(year)
		total_age += age
	return total_age // len(a)


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	sorted_data = sorted(a, key = lambda x:x[col])
	csv_file = open(fileName, 'w')
	for student in sorted_data:
		csv_file.write('{},{},{}\n'.format(student['First'], student['Last'], student['Email']))
	csv_file.close()



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
