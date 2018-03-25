from selenium import webdriver
from config import *
import os
import argparse
import time


parser = argparse.ArgumentParser()
parser.add_argument("--base_url", help="Set DEFAULT_BASE_URL for the tests.",)
parser.add_argument("--test", help="If specified a test name, runs a single test", default="all")
parser.add_argument("--browser", help="Run tests on the specified browser.", default=False)
args = parser.parse_args()

if args.base_url is not None:
    BASE_URL = args.base_url
else:
    BASE_URL = DEFAULT_BASE_URL

if BASE_URL == "":
    print("Set DEFAULT_BASE_URL in config.py")
    exit()

browsers = ["chrome"]
if args.browser:
    if args.browser == "chrome":
        browsers = ["chrome"]
    elif args.browser == "firefox":
        browsers = ["firefox"]
    elif args.browser == "all":
        browsers = ["chrome","firefox"]
    else:
        browsers = ["chrome"]

for browser in browsers:
    print("--------------------------------------------------\n")
    print("Started tests on " + browser + " browser")
    print("--------------------------------------------------\n")
    if browser == "chrome":
        driver = webdriver.Chrome("chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path='geckodriver')

    tests_to_run = []
    if args.test == "all":
        for file in [doc for doc in os.listdir("tests") if doc.endswith(".py") and doc != "__init__.py"
                                                           and doc != "base_test.py"]:
            tests_to_run.append("tests." + file.split(".")[0])
    else:
        tests_to_run = ["tests." + args.test.split(".")[0]]

    all_tests_start_time = time.time()

    for test_to_run in tests_to_run:
        this_test_start_time = time.time()
        current_test = getattr(__import__(test_to_run, fromlist=["Test"]), "Test")
        test = current_test(driver, BASE_URL, test_to_run)
        test.run()

        this_test_seconds_taken = time.time() - this_test_start_time
        if this_test_seconds_taken > 60:
            print("Time taken: " + str(this_test_seconds_taken / 60) + " minutes")
        else:
            print("Time taken: " + str(this_test_seconds_taken) + " seconds")

    all_tests_seconds_taken = (time.time() - all_tests_start_time)
    if all_tests_seconds_taken > 60:
        print("Time taken for all tests: " + str(all_tests_seconds_taken / 60) + " minutes")
    else:
        print("Time taken for all tests: " + str(all_tests_seconds_taken) + " seconds")

driver.quit()
