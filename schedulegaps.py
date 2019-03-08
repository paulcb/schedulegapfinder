from dateutil import parser

if __name__ == "__main__":
    
    person1 = []
    person1File = open('westschedule.txt', 'r') 
    for line in person1File:
        if line.strip():
            person1.append(parser.parse(line))
    p1Iter = iter(person1)

    person2 = []
    person2File = open('joeschedule.txt', 'r')
    for line in person2File:
        if line.strip():
            person2.append(parser.parse(line))
    p2Iter = iter(person2)

    #skip to gaps
    p1Iter.next()
    p2Iter.next()

    # get first times
    t1 = p1Iter.next()
    t2 = p1Iter.next()

    t3 = p2Iter.next()
    t4 = p2Iter.next()


    while True:

        if t2 > t3 and t2 <= t4:
            print('Schedule gap p1 ' + t1.strftime('%A %H%M ') + t2.strftime('%A %H%M'))
            print('Schedule gap p2 ' + t2.strftime('%A %H%M ') + t4.strftime('%A %H%M'))
            print('Duration ' + str(t2-t3))
            t1 = p1Iter.next()
            t2 = p1Iter.next()

        if t1 >= t3 and t1 <= t4:
            print('Schedule gap p1' + t1.strftime('%A %H%M ') + t2.strftime('%A %H%M'))
            print('Schedule gap p2' + t2.strftime('%A %H%M ') + t4.strftime('%A %H%M'))
            print('Duration' + str(t3-t1))
            t3 = p2Iter.next()
            t4 = p2Iter.next()

        if t2 < t4 and t2 <= t3:
            t1 = p1Iter.next()
            t2 = p1Iter.next()

        if t3 <= t1 and t3 < t2:
            t3 = p2Iter.next()
            t4 = p2Iter.next()

