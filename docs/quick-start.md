# Quick start

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
