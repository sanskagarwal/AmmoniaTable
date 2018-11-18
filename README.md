# Ammonia Table

It is a python script to find out properties of Saturated Ammonia and Superheated Ammonia, GUI presented using Tkinter.
It have the following features till now: 
  - Saturated Properties(using Pressure)
  - Saturated Properties(Using Temperature)
  - Superheated Properties(Using Temperature & Pressure)

## Features to Add:

  - Currently due to a small Dataset it shows properties to a limited extent, in future i am looking forward to deploy it for bigger Data(Using Machine Learning Probably)
  - Improve the GUI of currrent App by adding Latex and Fonts


## Installation

Ammonia Table Conversion project requires your PC to have python3 installed.

#### If you are using 'pip' package distribution, install following dependencies first:

```sh
$ pip install pandas
```

However if you are using Anaconda Distribution or any other popular distribution you should be good to go!
Run the following command
```sh
$ python <script_name>.py
```

For production environments...

```sh
$ pip install pandas
$ pip install pyinstaller
$ pyinstaller <script_name>.py
```
After Few Seconds it will create a folder named "dist", add both CSV files inside dist>ammoniaTable>..

For Linux Users
```sh
$ mv saturated.csv dist/ammoniaTable
$ mv superheated.csv dist/ammoniaTable
```
For Window Users
```sh
$ move saturated.csv dist\ammoniaTable
$ move superheated.csv dist\ammoniaTable
```

## License

MIT
