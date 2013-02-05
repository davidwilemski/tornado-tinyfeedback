tornado-tinyfeedback
====================

A tornado client for tinyfeedback

example:

```
from tornadotinyfeedback import Client

def callback(response):
    if response.code == 200:
        print 'data sent'
    else:
        print 'data error'

tf = Client('testing')
tf.send({'blah_metric': 10000}, callback)
```

For a more complete example see `examples/simple.py`.
