def fastq2fasta(input, output):
    try:
        inp = open(input)
    except IOError:
        print('could not open', input, 'for reading')
    try:
        out = open(output, 'w')
    except IOError:
        print('could not open', output, 'for writing')
    count = 0
    for line in inp:
        count += 1
        if count % 4 == 1:
            line = line[1:]  # get rid of the '@'
            out.write(">"+line)
        elif count % 4 == 2:
            out.write(line)
    inp.close()
    out.close()

fastq2fasta('SP1.fq', 'test.fa')

