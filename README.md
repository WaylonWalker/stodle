**Stodle**

Python module to keep windows running

Installation from cmd line
```
git clone https://github.com/WaylonWalker/stodle.git
cd ./stodle
python setup.py install
```

Usage

```
from stodle import stop_idle()
import time

def really_long_function()
    """
    needs to run without windows going into screensaver
    """

    for i in range(1000)
        time.sleep(100)
        stop_idle()

```