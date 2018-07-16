# Functions to count the number of sequences in a fastq or fasta file


def countFastq(name):  # assumes tha this is a proper fastq file
    count = 0
    try:
        f = open(name)
        for line in f:
            count += 1
        f.close()
        return int(count/4)
    except IOError:
        print('could not open file:', name, 'for reading')


def countFasta(name):
    import urllib.request
    import urllib.error
    count = 0
    if name.startswith('http://'):  # try to open URL
        try:
            f = urllib.request.urlopen(name)
        except urllib.error.URLError:
            print('could not open URL', name)
            return
    else:  # try to open local file
        try:
            f = open(name)
        except IOError:
            print('could not open file:', name, 'for reading')
            return
    for line in f:
        if type(line) is bytes:
            if line.startswith(b'>'):
                count += 1
            continue
        if line.startswith('>'):
            count += 1
    f.close()
    return count
