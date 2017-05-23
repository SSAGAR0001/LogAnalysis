#!usr/bin/env python
import psycopg2


def connect(database='news'):
    try:
        db = psycopg2.connect('dbname={}'.format(database))
        c = db.cursor()
        return db, c
    except:
        print 'Cannot Connect to the Database'


def articles_on_top():
    try:
        db, c = connect()
        q = "select * from toparticles"
        c.execute(q)
        ans = c.fetchall()
        print '\nTop Articles:'
        for x in xrange(0, 3):
            print '%s -- %s views' % (ans[x][0], ans[x][1])
        c.close()
        db.close()
    except:
        print 'error in creating view toparticles!!'


def authors_on_top():
    try:
        db, c = connect()
        q = "select * from topauthors"
        c.execute(q)
        ans = c.fetchall()
        print '\nTop Authors:'
        for x in xrange(0, len(ans)):
            print '%s -- %s views' % (ans[x][0], ans[x][1])
        db.commit()
        c.close()
        db.close()
    except:
        print 'error in creating view topauthors!!!'


def all_day_errors():
    try:
        db, c = connect()
        q = "select * from alldayerrors"
        c.execute(q)
        ans = c.fetchall()
        length = len(ans)/2
        date = []
        error = []
        for x in xrange(0, length):
            # Calculating percentage
            errorPercentage = float(ans[x][1] / float(ans[x+length][1])) * 100
            if errorPercentage > 1:
                date.append(ans[x][0])
                error.append(float(errorPercentage))
        print '\nDays on which more than 1% of requests lead to errors are:'
        for x in xrange(0, len(date)):
            print '%s -- %f' % (date[x], error[x])
        db.commit()
        c.close()
        db.close()
    except:
        print 'error in creating view alldayerrors!!!!'


if __name__ == '__main__':
    articles_on_top()
    authors_on_top()
    all_day_errors()
#!usr/bin/env python
import psycopg2


def connect(database='news'):
    try:
        db = psycopg2.connect('dbname={}'.format(database))
        c = db.cursor()
        return db, c
    except:
        print 'Cannot Connect to the Database'


def articles_on_top():
    try:
        db, c = connect()
        q = "select * from toparticles"
        c.execute(q)
        ans = c.fetchall()
        print '\nTop Articles:'
        for x in xrange(0, 3):
            print '%s -- %s views' % (ans[x][0], ans[x][1])
        c.close()
        db.close()
    except:
        print 'error in creating view toparticles!!'


def authors_on_top():
    try:
        db, c = connect()
        q = "select * from topauthors"
        c.execute(q)
        ans = c.fetchall()
        print '\nTop Authors:'
        for x in xrange(0, len(ans)):
            print '%s -- %s views' % (ans[x][0], ans[x][1])
        db.commit()
        c.close()
        db.close()
    except:
        print 'error in creating view topauthors!!!'


def all_day_errors():
    try:
        db, c = connect()
        q = "select * from alldayerrors"
        c.execute(q)
        ans = c.fetchall()
        length = len(ans)/2
        date = []
        error = []
        for x in xrange(0, length):
            # Calculating percentage
            errorPercentage = float(ans[x][1] / float(ans[x+length][1])) * 100
            if errorPercentage > 1:
                date.append(ans[x][0])
                error.append(float(errorPercentage))
        print '\nDays on which more than 1% of requests lead to errors are:'
        for x in xrange(0, len(date)):
            print '%s -- %f' % (date[x], error[x])
        db.commit()
        c.close()
        db.close()
    except:
        print 'error in creating view alldayerrors!!!!'


if __name__ == '__main__':
    articles_on_top()
    authors_on_top()
    all_day_errors()
