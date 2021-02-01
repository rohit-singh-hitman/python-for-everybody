import sqlite3
conn = sqlite3.connect('Counts.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Records')
cur.execute('CREATE TABLE Records(email TEXT,count INTEGER)')
fh = input('enter file:')
f=open(fh)
for line in f:
    line.rstrip()
    if not line.startswith('From'):
        continue
    p=line.split()
    q=p[1]
    cur.execute('SELECT count FROM Records WHERE email =?', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Records(?,1)',(email,))
    else:
        cur.execute('UPDATE Records SET count = count+1 where email = ?',(email,))
    conn.commit()
sqlstr = 'SELECT email,count FROM Records ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(row[0],row[1])
