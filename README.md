# Inventory challenge

The project is easily structured in several namespaces in the `redacted` module which provide functionality for solving the challenge in the main script.
The idea is to keep a clear separation of concerns and to leverage Python functional programming features, resulting in code easier to understand, extend, and maintain.

Here's a short description of each namespace functionality and intent.


| Namespace | Description                                       |
|-----------|---------------------------------------------------|
| api       | Contains definitions for interacting with the API.|
| logic     | Contains definitions for business logic.          |
| types     | Contains definitions of model entities.           |
| memory    | Main store for the challenge.                     |



Regarding the main script, it only contains two functions, `profit_scenario`, and `loss_scenario`.


## Running

In order to run the code. You may run `python3 main.py`

## Tests

I included some tests. In order to run them, you must install `pytest` and then run:

`python3 -m pytest` 


## How did I get to this solution?
I explored having an inventory that tracked each `Unit` separately and then correlating it with a `Sale` by using a UUID as a correlation id.
Complexity started to grow so I decided to better keep it simple and leverage the fact of the usage of WAC for calculations thus resulting in a simpler model.

For the state, I just use lists and derive the data that I need on demand. There was the option of using Dictionaries for keeping track of stock, but opted for the lists because of their practicality.
Since the state is abstracted away in the `memory` namespace, it would be very easy to change it to more efficient data structures should the need arise.


## Next steps
I would have liked to implement a more efficient data structure so I could index by date for future requirements, such as calculating profit/loss for a given date range.

