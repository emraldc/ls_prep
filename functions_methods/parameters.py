def say(msg1, msg2, msg3='dummy message', 
                    msg4='omitted message'):
    print(msg1)
    print(msg2)
    print(msg3)
    print(msg4)

say('a', 'b', 'c', 'd')
say('a', 'b', 'c')
say('a', 'b')
say('a', 'b', 'd')