import argparse
 
parser = argparse.ArgumentParser(description='encode text file.')
parser.add_argument('-p', dest='filepath', action='store', required=True, type=str, help='the directory of filename to encode')
args = parser.parse_args() 
filepath = args.filepath

def main():
	fr = open(filepath, 'rb')
	by = fr.read()
	add_head = by[:1]
	fr.close()

	fw = open(filepath,'wb')
	fw.write(add_head)
	fw.write(by)
	fw.flush()
	fw.close()

if __name__ == '__main__':
	main()
