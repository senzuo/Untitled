import argparse
 
parser = argparse.ArgumentParser(description='encode text file.')
parser.add_argument('-p', dest='filepath', action='store', required=True, type=str, help='the directory of filename to decode')
args = parser.parse_args() 
filepath = args.filepath

def main():
	fr = open(filepath,'rb')

	by = fr.read()
	by = by[1:]


	fw = open(filepath,'wb')
	fw.write(by)
	fw.flush()
	fw.close()

	fr.close()

if __name__ == '__main__':
	main()