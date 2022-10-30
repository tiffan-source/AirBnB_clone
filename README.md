AirBnB clone
============

The AriBnB clone project is a simple copy of the Airbnb website that implement features which covers all fundamental concepts of the higher level programming track. It is composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## The command interpreter

It defines one class, `HBNBCommand()`, which sub-classes the `cmd.Cmd` class.

This module defines abstractions that allows us to manipulate a powerful storage system (FileStorage / DB). This abstraction will also allow us to change the type of storage easily without updating all of our codebase.

It allows us to interactively and non-interactively:
    - Create a data model
    - Manage (create, update, destroy, etc) objects via a console / interpreter
    - Store and persist objects to a file (JSON file)

Usage example:

    $ ./console
    (hbnb)
    (hbnb) help
    Documented commands (type help <topic>):
    ========================================
    EOF  create  help  quit
    (hbnb)
    (hbnb) quit

    $