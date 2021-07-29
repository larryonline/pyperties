# Pyperties

a simple python `.properties` reader/writer

### How to use this
1. `pip install pyperties` 
2. do script
```shell
import pyperties

FILE_PATH="your .properties file"
value = pyperties.from(FILE_PATH).section('DataSection').get('DataKey')

```
