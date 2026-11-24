# API, I choose you!
A Pokemon themed python script to help others understand JSON and API handling. This repo uses the PokeAPI RESTful API website/interface (https://pokeapi.co/).

As you go through each example in the Python script, **remove** the `#` symbol before the code statements, so they don't stay as comments and to **be able to run them**!

## Before you start
 
1. Install **Python** (python.org).
2. Open **Visual Studio**, open a terminal, and check that it works:
```
python --version
```
or on macOS:
```
python3 --version
```
---

## WHO is JSON??
JSON (JavaScript Object Notation) is a **text format** for storing and exchanging data. Although its syntax is similar to the 'JavaScript Object' syntax, it is **language independent** (i.e. can be used in many languages).

**Look at this example**:
```
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
```
There are 3 properties written in **name/value pairs**:
- Each property has a name (“name”, “age”, “city”)
- Each property has a value (“John”, 30, “New York”)
- Names and values are separated by colons (`"name" : "John"`)
- Each name/value pair is separated using commas,  
except the last one (no trailing commas)
---

## Why use JSON?
Computers and applications often need to exchange data, and JSON provides a simple text format that many programming languages can read and create.

JSON is commonly used for:
- Sending data from a web server to a web page
- Sending data from a web page to a server
- Storing configuration data
- Saving structured data in files
- Exchanging data between applications

JSON is usually stored in `.json` files

---
## JSON Object Literals
This is a **JSON string**:

`'{"name":"John", "age":30, "car":null}'`

Inside the JSON string there is a **JSON object literal**:

`{"name":"John", "age":30, "car":null}`

(Notice that the **string** has **single quotation marks** encasing the object literal)

Also, notice that:
- A **JSON object** is written between **curly braces { }**.
- An object contains zero or more **properties**.
- Properties come in **key/value pairs** separated by **commas**, **no trailing commas**.
- Key names are strings enclosed in **double quotes**.
- Keys and values are separated by a **colon**.
---

### Accepted JSON values
JSON only has 6 supported value types:
<table>

<tr>
<th>Value</th>
<th>Example</th>
</tr>

<tr>
<td>String</td>
<td>"John"</td>
</tr>

<tr>
<td>Number</td>
<td>42</td>
</tr>

<tr>
<td>Boolean</td>
<td>true</td>
</tr>

<tr>
<td>Null</td>
<td>null</td>
</tr>

<tr>
<td>Object</td>
<td>{"name": "John"}</td>
</tr>

<tr>
<td>Array</td>
<td>[1, 2, 3]</td>
</tr>

</table>

---

### Nested values
Objects and arrays can contain other objects and arrays. This makes it possible to represent **complex data structures**.

Take a look at this example:
```
{
  "name": "John",
  "age": 30,
  "address": {
	"city": "New York",
	"country": "USA"
  },
  "hobbies": [
	"Reading",
	"Cycling",
	"Photography"
  ]
}
```
Here `"address"` contains another object:

 `{"city": "New York", "country": "USA"}`
 
 Additionally, `"hobbies"` contains an array:

 `["Reading", "Cycling", "Photography"]`

 ---

## JSON in Python
Now that we've identified how JSON looks (not a person btw!), let's go over how to **convert** JSON to Python and vice versa

Before we start, we need to import Python's built in package `json` to work with JSON data:
```
import json
```

---
### Converting from JSON to Python
We can **_parse_** (convert) JSON string to Python using the `json.loads()` method. The result would be a Python **dictionary**.

**Check out 'JSON example 1' in the Python script!**

---

### Converting from Python to JSON
We can convert a Python object into a JSON string using the `json.dumps()` method.

**Check out 'JSON example 2' in the Python script!**

When converting from Python to JSON, **Python objects** get converted into the **JSON equivalent**:

<table>

<tr>
<th>Python</th>
<th>JSON</th>
</tr>

<tr>
<td>dict</td>
<td>Object</td>
</tr>

<tr>
<td>list</td>
<td>Array</td>
</tr>

<tr>
<td>tuple</td>
<td>Array</td>
</tr>

<tr>
<td>str</td>
<td>String</td>
</tr>

<tr>
<td>int</td>
<td>Number</td>
</tr>

<tr>
<td>float</td>
<td>Number</td>
</tr>

<tr>
<td>True</td>
<td>true</td>
</tr>

<tr>
<td>False</td>
<td>false</td>
</tr>

<tr>
<td>None</td>
<td>null</td>
</tr>
</table>

---

### Formatting JSON result
Notice how in the last example, the JSON string looked neat when we printed it. However this isn't the case with **large** JSON string.

**For example, check out the 'JSON example 3' in the Python script!** <br>Notice how it's very hard to read, especially with no indentations or line breaks.

Thankfully, the `json.dumps()` method has the `indent` parameter to define the **number of indents**, making it **easier to read** the result.
<br>**Check out 'JSON example 4' in the Python script!**

Let's go over **APIs** now!

---

## What are APIs?
**Application Programming Inteface** (API) is a set of rules that allows different software applications to **communicate with each other**, by requesting **data** or **functionality**.

**Example**: A weather app uses a **Weather API** to **fetch** and display the current temperature and weather conditions for a location.

---
### How an API works
An API acts as an interface between a client and a server, allowing them to communicate and exchange data. It receives a request from the client, processes it, and returns an appropriate response.

**Types of API Architectures**:
- **REST** (**Representaional State Transfer**): an architetural style that uses **HTTP methods** for communication between clients and servers. (_This is the one we'll be going over!_)
- **SOAP** (**Simple Object Access Protocol**): a protocol that uses **XML-based** messages  and follows **standardized rules** for communication between applications.
- **GraphQL**: a **query language** and API specification that allows clients to request **only the data they need**.
- **gRPC** (Google Remote Procedure Call): **high-performance** RPC framework that enables communication between **distributed servers** using **Protocol Buffers** (**Protobuf**).

---
### Too much jargon!!
Basically, APIs allow applications to **communicate and exchange data**, usually in the **JSON format**. This is done through **requests** and **responses**.

There are many types of APIs, but the one we're going to talk about is **REST API**.

**Recall back the JSON we got from 'JSON example 4!'**

---
## REST API
As we mentioned before, REST API uses **HTTP methods** such as **GET**, **POST**, **PUT**, **PATCH**, and **DELETE** to work with resources, which can be accessed using **URLs**.

**Resources** are data or entities that an API provides **access** to. Each resource is identified by a **unique URI** (Note URI and **not URL**!).
<br>**For example**:
- `/users` represents a collection of users.
- `/users/101` represents a specific user.

---
### The main 4 points about REST
1. **Endpoint**: a specific address **where** an application can send a request. For example, the endpoint (https://pokeapi.co/api/v2/pokemon/pikachu) might retrieve data about Pikachu.

2. **HTTP method**: tells the server what the application wants to do. To better understand this, let's say we have a bank endpoint (`https://bank.com/accounts/balance`):

    <table align = "center">

    <tr>
    <th>Method</th>
    <th>Purpose</th>
    <th>Example</th>
    </tr>

    <tr>
    <td>GET</td>
    <td>Retrieve Information</td>
    <td>Get a customer's account balance</td>
    </tr>

    <tr>
    <td>POST</td>
    <td>Submit Information</td>
    <td>Create a new account</td>
    </tr>

    <tr>
    <td>PUT</td>
    <td>Replaces an existing resource</td>
    <td>Replace a customer's account details</td>
    </tr>

    <tr>
    <td>PATCH</td>
    <td>Partially update an existing resource</td>
    <td>Update only a customer's email address</td>
    </tr>

    <tr>
    <td>DELETE</td>
    <td>Remove Information</td>
    <td>Delete an account</td>
    </tr>

    </table>
<br>

3. **JSON**: the format used to send information between applications.

4. **Response**: After recieving and processing the requests, the server sends a response. For example, using the previous Pikachu endpoint, we can get data about Pikachu in the form of a **JSON**.  
  
<br> In addition, the response also has an **HTTP status code**. There is a large number of status codes, but here are some of the famous ones:  
<table align = "center">

<tr>
<th>Status code</th>
<th>Meaning</th>
</tr>

<tr>
<td>200</td>
<td><b>OK</b>: request successful</td>
</tr>

<tr>
<td>201</td>
<td><b>Created</b>: resource created successfully</td>
</tr>

<tr>
<td>400</td>
<td><b>Bad Request</b>: invalid input</td>
</tr>

<tr>
<td>404</td>
<td><b>Not Found</b>: resource doesn't exist</td>
</tr>

<tr>
<td>500</td>
<td><b>Internal Server Error</b>: server-side problem</td>
</tr>

</table>

---
### JSON validation and errors
Recieving valid JSON doesn't automatically mean the data inside it is acceptable. For example, imagine an API expects a person's name and age:

<table align = "center">

  <tr>
  <th>Problem</th>
  <th>Example</th>
  <th>What's wrong?</th>
  </tr>

  <tr>
  <td>Malformed JSON</td>
  <td><code>{"age": 21,}</code></td>
  <td>Invalid JSON syntax (trailing comma)</td>
  </tr>

  <tr>
  <td>Missing Field</td>
  <td><code>{"name": "Mohamed"}</code></td>
  <td>The required <code>age</code> field is missing</td>
  </tr>

  <tr>
  <td>Wrong data type</td>
  <td><code>{"age": "21"}</code></td>
  <td>Age is a string, not a number</td>
  </tr>

  <tr>
  <td>Invalid value</td>
  <td><code>{"age": -5}</code></td>
  <td>Age is a number, but negative values aren't allowed</td>
  </tr>

  <tr>
  <td>Null value</td>
  <td><code>{"age": null}</code></td>
  <td>The field exists but has no value</td>
  </tr>

  </table>

---
## Accessing REST APIs in Python
Finally, we can go over to the code!! Before we start, we'll need to **install** an **external library** called `requests`, which allows our Python script to make **web/internet requests** as if we were the browser ourselves.  
To install it, we're going to use `pip`:
```
py -m pip install requests
```
or on macOS
```
python3 -m pip install requests
```
---
### The 'requests' function
We can use the `requests` function to implement the HTTP methods we mentioned previously. Let's start with the GET method:
```
response = requests.get("URL")
```
This function requests data from a URL, like how a GET method would.  
Using the URL of a Pokemon of your choice, try **printing the result in 'API example 1' in the Python Script!** (_take note of the result!_)

To actually see the data, we'll have to use the `.json()` method on the response:
```
print(response.json())
```
To 'pretty print' it, we can use the `json.dumps()` function and apply indentation:
```
print(json.dumps(response.json(), indent = 4))
```
**Try playing around with 'API example 1' some more to fully grasp the concept!** Maybe try using another pokemon, or another resource (e.g.`/locations`). You can check the documentation on the website!.

Since what we get from the `.json()` function is a Python dict, we can use dict functions on the response variable. **Check out 'API example 2!'**

---
### More things we can do with requests
- `response.status_code` returns the **status code** of the request. We can use `response.raise_for_status()` to **raise an error** if the status code isn't between 200 - 299 rather than running the rest of the code and failing. **Check out 'API example 3!'**

- We can get the request's header using `response.headers` (or `respone.headers.get("...")` if you want a specific header). This will be more useful when using **authorization**. Try **printing a request header** and see what it looks like.

- We can set **query paramters** (e.g. something like `page=2` in the url) for the request: `requests.get(url, params= ...)`, where paramters would usually be in the form of a dictionary. **Check out 'API example 4!'**

- Sometimes, we'd need **authorization** to access an API. For example, we could be asked to provide a '**Bearer token**' in the request header. To better understand how it looks like, **Check out 'API example 5!'**
---
### Other HTTP methods
To use POST, we can perform `requests.post(url, json= ...)`, where json is what we're sending to the server. **Check out 'API example 6!'**

To use DELETE, we can perform `requests.delete(url)`. **Check out 'API example 7!'**

To use PUT and PATCH, we can perform `requests.put(url, data= ...)` and `requests.put(url, data= ...)`, respectfully, where data is the json we want to update. **Check out 'API example 8!'**