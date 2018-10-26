import numpy

def readFileAndReturnItsContent(filename):

	f = open(filename , "r")

	contents = f.read()

	f.close()

	return contents





def main():

	# f  = open("input.txt", "r")

	contents = readFileAndReturnItsContent("input.txt");

	print(len(contents))

	matrix = []

	for line in contents:

		row = []

		for word in line.split():

			print(word);

			if word == "":
				continue
			row.append(int(word))

		matrix.append(row)

	print(matrix)

	a = numpy.array([[1,2],[3,4]])

	print(numpy.linalg.det(a))

 	# print(det)





if __name__ == "__main__":

	main()
