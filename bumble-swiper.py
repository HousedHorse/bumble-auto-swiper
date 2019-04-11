#! /usr/bin/python3
from selenium import webdriver
from selenium.common.exceptions import *

import argparse

def log_in_with_facebook(driver, email, password):
    while True:
        try:
            driver.find_element_by_xpath("//div[contains(@class, 'button--provider-facebook')]").click()
            break
        except NoSuchElementException:
            pass

    # switch to facebook window
    driver.switch_to.window(driver.window_handles[1])

    # try to enter email until it loads
    while True:
        try:
            driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
            break
        except NoSuchElementException as e:
            pass

    # enter password and click submit
    driver.find_element_by_xpath("//input[@id='pass']").send_keys(password)
    driver.find_element_by_xpath("//input[@id='u_0_0']").click()

    try:
        # try to click continue until it loads
        while True:
            try:
                driver.find_element_by_xpath("//button[contains(text(), 'Continue as')]").click()
                break
            except NoSuchElementException:
                pass
    except:
        pass

    # back to main window
    driver.switch_to.window(driver.window_handles[0])

def dismiss_match(driver):
    try:
        driver.find_element_by_xpath("//div[contains(@class, 'button')//span[contains(text(), 'Continue Bumbling')]]/parent::*/parent::*/parent::*").click()
    except:
        pass

def swipe_right(driver):
    while True:
        # swipe right if the window is loaded
        try:
            driver.find_element_by_xpath("//div[contains(@class, 'encounters-action--like')]").click()
            return True
        except NoSuchElementException:
            pass
        except ElementClickInterceptedException:
            dismiss_match(driver)
            return True

        if all_done(driver):
            return False

def all_done(driver):
    # check to see if we are all caught up
    try:
        driver.find_element_by_xpath("//*[contains(text(), 'all caught up')]")
        return True
    except NoSuchElementException:
        pass
    try:
        driver.find_element_by_xpath("//*[contains(text(), 'bees in your area')]")
        return True
    except NoSuchElementException:
        pass

    return False;

if __name__ == "__main__":
    # parse arguments
    parser = argparse.ArgumentParser(description="Auto swiper for bumble. Pass your Facebook email and password.")
    parser.add_argument('email', metavar='email', type=str, nargs=1,
            help='Your Facebook email')
    parser.add_argument('password', metavar='password', type=str, nargs=1,
            help='Your Facebook password')

    args     = parser.parse_args()
    email    = args.email
    password = args.password

    # open driver
    driver = webdriver.Firefox()
    driver.get("https://bumble.com/login")

    log_in_with_facebook(driver, email, password)

    # keep swiping right until we're caught up
    while True:
        if not swipe_right(driver):
            print("All caught up!")
            break

    driver.close()
