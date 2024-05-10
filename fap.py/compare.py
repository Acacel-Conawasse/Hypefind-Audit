def compare_files(file1, file2):
    # Open the two files to read from
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # Read the lines from each file
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # Open the output files for writing results
    with open('matching.txt', 'w') as match, \
         open('not_matching1.txt', 'w') as not_match1, \
         open('not_matching2.txt', 'w') as not_match2:

        # Iterate through both lists of lines up to the length of the longest list
        max_len = max(len(lines1), len(lines2))
        for i in range(max_len):
            line1 = lines1[i].strip() if i < len(lines1) else ""
            line2 = lines2[i].strip() if i < len(lines2) else ""

            # Compare lines from both files
            if line1 == line2:
                match.write(line1 + '\n')
            else:
                if line1:
                    not_match1.write(line1 + '\n')
                if line2:
                    not_match2.write(line2 + '\n')

compare_files('C:/Users/omalomo3/Desktop/Hypefind Audit/fap.py/jhworks.txt', 'C:/Users/omalomo3/Desktop/Hypefind Audit/fap.py/central.txt')
