import zipfile36 as zipfile
import time

filename = input("Put the file name here: ")
zipFile = zipfile.ZipFile(filename)

global result
result = 0

global tried
tried = 0

counter = 0

if not zipFile:
    print('The zipped file is not password protected you can access it.')
else:
    startTime = time.time()
    wordListFile = open("wordlist.txt", "r", errors="ignore")
    body = wordListFile.read().lower()
    words =  body.split('\n')
    # duration = endTime - startTime
    for i in range(len(words)):
        word = words[i]
        password = word.encode('utf-8').strip()
        counter +=1
        print("Trying to get password by: {}".format(word))
        try:
            with zipfile.ZipFile(filename, 'r') as zf:
                zf.extractall(pwd=password)
                print("Valla!,you have cracked the password after " + str(counter) + ' tries. ')
                endTime = time.time()
                result =1
                duration = endTime-startTime
                print("Crackec in " + str(duration) + 'seconds')
            break
        except:
            pass
    