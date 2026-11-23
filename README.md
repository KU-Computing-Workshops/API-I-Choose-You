# API, I choose you!
A Pokemon themed python script to help others understand JSON and API handling. This repo uses the PokeAPI RESTful API website/interface (https://pokeapi.co/).

As you go through each example in the Python script, **remove** the `#` symbol before the code statements, so they don't stay as comments and to **be able to run them**!

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