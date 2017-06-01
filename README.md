# goPyServer
---
This is Python JSON-RPC Server Library which can accept JSON-RPC calls from Golang Client program and hopefully, Python as well.

With this library, you can cross-communicate with Golang as a Client in a flick.

#### For a quick demo for this library, please visit this [LINK](chawlanikhil24.blogspot.com).
---

**Why I developed this library?**

Since, I've working on Python for 2 years and many of my current projects are based on Python. Now, since just for variety and enthusiasm I wanted to adapt myself to a compiler based language and so I heard about [Golang](chawlanikhil24.blogspot.com). It was new and I kinda felt fun doing it. Now, I wanted to merge my Python projects with Golang. And as said,


### *"Necessity is the mother of invention(innovation)"*

And here I developed a library for those who are keen to experiment with both **Python** & **Golang** .

---

### Now, **How to use this library?**

Follow these steps and you are on:

  * Clone the library from github
      ```
        git clone https://github.com/chawlanikhil24/goPyServer.git
      ```
  * Install this library in your system, preferably in a Virtual environment
      ```
        python setup.py install
      ```
  * Import this library in your program
      ```
        import goPyServer as GP
      ```
  * Define your functions
      ```
        def f1():
          return "function 1"

        def f2():
          return "function 2"
      ```
  * Initialise the Object of Python Server(**DEFAULTS->** "Host":"localhost","Port":9000,"bufferSize":1024,"Listen":4)
      ```
        obj = GP.pyServ()
      ```
  * Register your functions with the RPC Server
      ```
        obj.register_function(f1)
        obj.register_function(f2)
      ```
  * Now, Connect() to the Socket Server at the mentioned address
      ```
        obj.connect()
      ```
  * Finally,Run the RPC() Server
      ```
        obj.RPCServer()
      ```
  * Now, from any site/terminal, you can remotely make RPCs using [Golang library](https://github.com/chawlanikhil24/gopy)

---

[Here](https://github.com/chawlanikhil24/gopy/tree/master/example), you can find the running example for Python-Golang Cross Communication.

# ENJOY
