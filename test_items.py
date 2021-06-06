import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket(browser):
    browser.get(link)
    time.sleep(3)
    button_add_to_basket = len(browser.find_elements_by_class_name('btn.btn-lg.btn-primary.btn-add-to-basket'))
    assert button_add_to_basket == 1, 'Item not found'
