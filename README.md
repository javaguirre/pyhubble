# Pyhubble

Python client for [hubble](https://github.com/jaymedavis/hubble), the terminal dashboard

![1427049686](https://cloud.githubusercontent.com/assets/488556/6770784/8305fb58-d0cb-11e4-82f7-e2932671da39.png)

## Installation

    pip install pyhubble

## Usage

Import the client

```python
    from pyhubble import Hubble
```

Initialization and sending values

```python
    hubble = Hubble('http://localhost:9999/')
    hubble.send({'label': 'Test', 'value': 1, 'column': 0})
```

Increment/decrement a label

```python
    hubble.increment('Test')  # Increments the value of this label
    hubble.decrement('Test')  # Decrements the value of this label
```


## TODO

Poll implementation
Unittest
High, low and screen properties
