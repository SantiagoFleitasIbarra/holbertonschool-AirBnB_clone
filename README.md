
# AirBnB CLone - The console
![AirBnB](https://i.imgur.com/Nl8vN2G.jpg)


## Introduction


Team project to build a clone of AirBnB.

In this project, the main objective is to create a console. This means that we will build a command interpreter that  will have the functionality to manage the abstraction between objects and how they are stored.


This console will perform the following tasks:

- Create a new object
- Retrieve an object from file
- Perform operations on objects
- Destroy or delete an object


## Instalation

```bash
git clone https://github.com/SantiagoFleitasIbarra/holbertonschool-AirBnB_clone.git
```

change to the `AirBnb` directory and run the command:

```bash
 ./console.py
```


### How used the console

The interactive mode involves real-time communication where the user can give instructions and receive immediate responses. Meanwhile, the non-interactive mode implies that the program runs autonomously, without the need for constant user intervention.

In interactive mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

in Non-interactive mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Examples

* Start the console in interactive mode:

```bash
$ ./console.py
(hbnb)
```

* Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

* Quit the console:

```bash
(hbnb) quit
$
```


### Testing

All the tests can be found in the folder named 'tests'.


### Tasks

Madatory:

| Name | Description |
| ------ | ------ |
| 0. README, AUTHORS | Write a README.md, You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository |
| 1. Be Pycodestyle compliant! | Write beautiful code that passes the Pycodestyle checks. |
| 2. Unittests | All your files, classes, functions must be tested with unit tests, `python3 -m unittest discover tests` |
| 3. BaseModel | Write a class BaseModel that defines all common attributes/methods for other classes:models/base_model.py. Public instance attributes: id, created_at, updated_at, __str__. Public instance methods: save(self), to_dict(self). |
| 4. Create BaseModel from dictionary | Now it’s time to re-create an instance with this dictionary representation. |
| 5. Store first object | Now we can recreate a BaseModel from another one by using a dictionary representation |
| 6. Console 0.0.1 | Write a program called console.py that contains the entry point of the command interpreter |
| 7. Console 0.1 | Update your command interpreter (console.py) to have these commands |
| 8. First User | Write a class User that inherits from BaseModel |
| 9. More classes! | Write all those classes that inherit from BaseModel |
| 10. Console 1.0 | Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review. Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously. No unittests needed for the console


