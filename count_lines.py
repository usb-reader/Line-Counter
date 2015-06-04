import os

def main():
	directory=str(raw_input("Directory: "))
	recursive_traversal=str(raw_input("Recursive Traversal? (y or n): "))
	file_exts=str(raw_input("File extensions (separate by comma): "))

	file_exts=handle_file_exts(file_exts)

	count= count_lines(directory, file_exts, recursive_traversal.lower())
	print "Count: "+str(count)


#turns "py,cpp,docx" into ["py", "cpp", "docx"]
def handle_file_exts(file_exts):
	temp=file_exts.split(",")

	new_list=[]
	for ext in temp:
		ext=ext.strip()

		if "." not in ext:
			ext="."+ext

		new_list.append(ext)

	return new_list

def count_lines(cur_dir, file_exts, recursive_traversal):
	count=0
	file_list=os.listdir(cur_dir)

	for x in range(0, len(file_list)):

		#recursively traverses directories if user wants
		if os.path.isdir(cur_dir+"/"+file_list[x]) and recursive_traversal=="y":
			count+=count_lines(cur_dir+"/"+file_list[x], file_exts, recursive_traversal)
		elif os.path.isfile(cur_dir+"/"+file_list[x]):

			#only considers file with one of the mentioned file extensions
			valid_file=False
			for ext in file_exts:
				if ext in file_list[x]:
					valid_file=True

			if valid_file:
				opened=open(cur_dir+"/"+file_list[x], 'r')
				print "opened: "+str(cur_dir)+"/"+str(file_list[x])
				for y in opened:
					count+=1
	return count


if __name__=="__main__":
	main()