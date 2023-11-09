def word_list(path = 'words.txt'):
    words=open(path,encoding='utf8')
    wordslist=words.read().upper().splitlines()
    words.close()
    return wordslist
def records(record, path='record.txt'):
    rec=open(path,mode='r+')
    cur_rec=int(rec.readline())
    cur_rec=max(cur_rec,int(record))
    rec.seek(0)
    rec.write(str(cur_rec))
    return cur_rec

