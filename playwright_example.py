from playwright.sync_api import Page, expect, sync_playwright
import base64
import os
import random
import re

# folders = os.listdir('signals')

def test_usage(page: Page):
    
    page.goto('https://the-internet.herokuapp.com/') #URL
    print('success')
    print(page)
    page.screenshot(path='website.png')
    try: 
        page.click("a[href='/basic_auth']")
        #whenever login window pops up, the context credentials will be filled in
        page.screenshot(path='/images/auth_page.png')
        #if no pop up window, regular login page:
            # page.wait_for_selector('#login', timeout=2000)
            # # Fill in the login credentials
            # page.fill('#login', username)
            # page.wait_for_selector('#password', timeout=2000)
            # # page.wait_for_timeout(10000) 
            # page.fill('#password', password)
            # page.wait_for_timeout(2000) 
            # print(username)
            # print(password)
            # page.screenshot(path='login_trial.png')

        page.go_back() #go back to main menu
        page.screenshot(path='/images/go_back.png')
        #Go to Add/Remove Elements
        page.click("a[href='/add_remove_elements/']")
        page.screenshot(path='/images/add_remove_elements_page.png')
        page.click("button[onclick='addElement()']")
        page.screenshot(path='/images/add_first_element.png')
        page.click("button[onclick='addElement()']")
        page.screenshot(path='/images/add_second_element.png')
        page.click("button[onclick='deleteElement()']")
        page.screenshot(path='/images/deleted_1_element.png')

        page.go_back()
        page.click("a[href='/upload']")
        page.screenshot(path='/images/upload_page.png')
        #Upload your file
        page.wait_for_selector("input#file-upload", state="visible")
        file_path = os.path.abspath("example_text.rtf")
        print(file_path)
        page.set_input_files("input#file-upload", file_path)
        page.screenshot(path='/images/chose_example_file.png')
        page.click("input#file-submit")
        page.screenshot(path='/images/uploaded_file.png')
        print(f"Successfully uploaded file: {file_path}")
        print(page.text_content("h3")) 

        page.go_back()
         
        # page.click('.checkbox input[type="checkbox"]')
        # page.wait_for_timeout(2000) 
        # # Click the login button in the popup
        # page.click('#loginButton', timeout = 2000)

        # # Wait for navigation to complete
        # page.wait_for_timeout(3000) 
        # error_message = page.query_selector('#loginError')

        # if error_message:
        #     print("Login failed. Incorrect username or password.")
        #     page.screenshot(path='login_error.png')
        # else:
        #     print("Login successful.")

        #     # Wait for a short duration for navigation to complete
        #     page.wait_for_timeout(2000)  # Wait for 5 seconds (adjust as needed)

    except Exception as e:
        print(e)
    # page.click('#loginButton'timeout = 60000)
    # page.click('#loginButton')
    # page.wait_for_timeout(2000) 
    # # Save screenshot
    # page.screenshot(path=f'press_recalculate.png')
    
    # page.click('i#menuBars')

    # page.screenshot(path=f'press_recalculate_2.png')

    # page.wait_for_selector('.app-menu__link', timeout=3000)

    # page.click('span.app-menu__link:has-text("Сигналы")')
    # page.wait_for_timeout(2000)

    # page.screenshot(path=f'press_recalculate_3.png')
    # for i in range(1410, 1489):
    #     print(i)
    #     page.fill('input[placeholder="appointmentId"]', f'{i}')

    #     page.wait_for_timeout(2000)
    #     page.screenshot(path=f'screenshots_2/press_recalculate_4.png')
    #     page.click('button.button.is-info:has-text("Поиск")')
    #     page.wait_for_timeout(2000)
    #     page.screenshot(path=f'screenshots_2/press_recalculate_5.png')
   
username = "admin"
password = "admin"

with sync_playwright() as p:
    browser = p.chromium.launch()

    context = browser.new_context(ignore_https_errors=True,
                                    http_credentials={"username": username, "password": password})
    
    page = context.new_page()

    test_usage(page)

    browser.close()


