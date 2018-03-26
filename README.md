# Signup Page Tests

Prerequisites for running these tests
----------
- python3, selenium


Versions I was using
----------
`Python 3.6.4`,

`Selenium 3.11.0`

`Chrome Version 64.0.3282.186 (64-bit)`

`Firefox 59.0.1 (64-bit)`


How to run the tests
---------
To run on all tests on all browsers (firefox and chrome)
```
python run.py --test all --browser all
```
To run all tests on Chrome
```
python run.py --test all --browser chrome
```
To only run one test (right now there is only one file though)
```
python run.py --test "signup_page_tests.py"
````
To specify a browser (by default it is chrome)
```
python run.py --test all --browser chrome
python run.py --test all --browser firefox
```