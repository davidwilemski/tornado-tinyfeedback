
import tornado.ioloop
from tornadotinyfeedback import Client

def func():
    tf = Client('testing')
    tf.send({'blah_metric': 10000}, lambda x: x)
    end_loop()

def end_loop():
    loop = tornado.ioloop.IOLoop.instance()
    loop.stop()

if __name__ == '__main__':
    func()
    loop = tornado.ioloop.IOLoop.instance()
    loop.start()
