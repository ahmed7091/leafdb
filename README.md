# Local LeafDB 🍃

[![python](https://img.shields.io/badge/Python-3.19%2B-green/?logo=python&logoColor=lightblue)](https://www.python.org) 
[![JavaScript](https://img.shields.io/badge/JavaScript-ES16-pink/?color=A300FF&logo=JavaScript)](https://tc39.es/ecma262/) 
[![Node.js](https://img.shields.io/badge/node-24.14.0-white/?color=blue&logo=node.js)](https://nodejs.org/)


> A modern, simple, object-oriented, experimental database, yet fast & easy-to-use.

---
  
# Content 🍃

- [overview](#overview)
- [Features](#features)
- [initialization](#initialization)
- [basic usage](#basic-usage)
  - [python](#python)
  - [JavaScript](#JavaScript)
- [LeafDB tools](#tools)

---

<h2 id="overview">Overview 🧩</h2>

  
<p align=center>LeafDB is an experimental (not production-ready) API that you can communicate with using HTTP requests, with any language in an object-oriented way</p>


---


<h2 id="features">Features 🚀</h2>

* **Multi-language support**: You can communicate with it using any langauge.

* **Available offline**: You can communicate with LeafDB completely offline.

* **Flexible**: leafDB accepts any type of key & value, which makes it less prone to errors.

---


<h2 id="initialization">How to initialize LeafDB</h2>
To setup LeafDB local build, you can clone it using `git CLI` tool by cloning the repo from github, and adding it's tools to your project.


1. Go to your project path if you haven't:
```bash
cd path/to/project
```
2. Clone the repo from github by `git CLI`:
```bash
git clone https://github.com/ahmed7091/leafdb.git
```

3. go to the leafdb project folder & run the script using `uvicorn`:
```bash
cd ./leafdb/src/leafdb/project
uvicorn main:app --port 8000 # Specify any port here
cd - # Return back
```
4. Declare the port in your project:

  python:
```python
from leafdb.leafdb import Leafdb

leafdb: Leafdb = leafdb()
leafdb.set_port(PORT)
```

  JavaScript: 
```javascript
// ES module
import Leafdb from "./leafdb/leafdb.js";
// CommonJS
const Leafdb = require("./leafdb/leafdb.js").default;

const leafdb = new Leafdb();

leafdb.setPort(PORT)
```
PORT is the port you specified in the terminal.
The default port is 8000, but if you ever changed it, you Must declare it otherwise the compiler will fail to establish a connection.


---


<h2 id="basic-usage">Basic usage</h2>
  
<h3 id="JavaScript">Using Javascript</h3>

```javascript
// as an ES module
import Leafdb from "./leafdb/leafdb.js";
// as a commonJS
const Leafdb = require("./leafdb/leafdb.js").default;

// Setup
const leafdb = new Leafdb();
leafdb.setPort(5000);

// Using async function because most leafdb methods are async
async function main(){
  await leafdb.insert({ 
    "message": "Thanks for using our API.", 
    "status_code": 200 
  })
  const data = await leafdb.view(); // { "message": "Thanks for using out API.", "status code": 200 }
  
  const message = await leafdb.view("message"); // "Thanks for using our API."
  
  await leafdb.del("status_code") // status_code field is no longer in the database
  
  await leafdb.edit("message", "LeafDB is a great database for experiments & learning.") 
  
  const newData = await leafdb.view();
  
  console.log("New data is: ", newData) // 'New data is: { "message": "LeafDB is a great database for experiments & learning." }'
}
main();

```

<h3 id="python">Using Python</h3>

```python
from leafdb.leafdb import Leafdb

leafdb: Leafdb = Leafdb()

leafdb.set_port(5000)

# Adding some data
leafdb.insert({
    "product": "Laptop",
    "price": 899.99,
    "sold": False,
    "tax": "8%"
})

# Viewing all data
data: dict = leafdb.view() # {"product": "Laptop", price: 899.99, "sold": False, "tax": "8%"}

# Viewing specific data
product = leafdb.view("product")
print(product) # 'Laptop'

leafdb.edit("sold", True)

leafdb.delete("tax")

new_data: dict = leafdb.view()

print("New data: ", new_data) # 'New data: {"product": "Laptop", "price": 899.99, "sold": True}'
```

<h2 id="tool">LeafDB tools</h2>

Here is a table of the functions available in LeafDB tools to [use](#basic-usage) (naming convension changes depending on the language): 
| name    | method | type  | usage    |
| ----    | -----  | ----- | -------- |
| setport | none   | sync  | Sets the dafault port to send requests to         |
| view    | GET    | async | returns `data` value if given, else returns all the database. |
| insert  | POST   | async | inserts the provided dict/object to the database. |
| delete(del in JS)| DELETE | async | Deletes the field with the provided key |
| edit    | PUT    | asnyc | Changes `key`'s value to `value`             |
| geturl  | none   | sync  | Returns the current URL of the API |