## What is serialization?

**Serialization** is converting data from the form in which they are processed inside one program to the interchangable format. The interchangable format allows to store that data outside the program and to send it between different enviroments and different programs. It is important that interchangable format allows data to be converted back to the structured form suitable for processing by programs - this operation is called **deserialization**, and it's basically the reverse of serialization.

## JSON

JSON is a popular interchangable data format. It's human readable and machine parsable as well.
**JSON** stands for **J**ava**S**cript Object Notation.
This format is often used for serialization.

## Python built-in serialization methods

Based on [this source](https://docs.python-guide.org/scenarios/serialization/).

## Serializing text

### Simple file (flat data)

#### repr
Takes a single object, returns a printable form of an input.

#### ast.literal_eval
Parses and evaluates expressions for Python datatype.

### CSV file (flat data)
A Python module that allows to read (deserialize) and write (serialize) data in CSV format.

### YAML (nested file)
A third-party module to read and write YAML data.

### JSON file (nested data)
json Python module allows to read and write json.

### XML (nested data)
xml package allows to deserialize XML interchangable format.

## Serializing binary data

### NumPy Array (flat data)
NumPy arrays can be used to serialize and deserialize data to and from byte representation.

### Pickle (nested data)
This is a native Python module for data serialization and deserialization.


## pydantic

**pydantic** is a Python tool intended mainly for data validation. Though as a very important and useful side effect it provides built-in serialization routines.
To use pydantic, you should create at least one class inhereting from pydantic BaseModel. While dealing with the objects of this class pydantic will provide data validation for fields (class properties). See [example](../notebooks/pydantic_examples_nb.py).

### Serialization with pydantic

pydantic also provides and ability to serialize objects of its classes that are based on pydantic base model to JSON format. This process it described in pydantic documentation [here](https://pydantic-docs.helpmanual.io/usage/exporting_models/#modeljson). In my jupyter notebook you can see [the example](../notebooks/pydantic_examples_nb.py) of this operation.

There is also an option to serialize models, not objects, to JSON Schema format. JSON Schema describes a model of data representation in JSON for particular context. As well pydantic models do the same for data in Python program, so this option is kind of expected. You can see some exampes [here](https://pydantic-docs.helpmanual.io/usage/schema/).




