from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()



def test_add_to_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    text_sauce_labs_backpack_before = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link'] div[class='inventory_item_name ' ]").text

    add_to_cart_button_sauce_labs_backpack = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button_sauce_labs_backpack.click()

    button_cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    button_cart.click()

    text_sauce_labs_backpack_after = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link'] > div[class='inventory_item_name' ]").text
    #time.sleep(5)

    assert text_sauce_labs_backpack_before == text_sauce_labs_backpack_after
    driver.quit()








