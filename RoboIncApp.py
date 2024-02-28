from robocorp.tasks import task
from robocorp import browser
from RPA.PDF import PDF
import os



def open_the_intranet_website():
    """Navigates to the given URL"""
    browser.goto("https://robotsparebinindustries.com/")

def log_in():
    """Fills in the login form and clicks the 'Log in' button"""
    page = browser.page()
    page.fill("#username", "maria")
    page.fill("#password", "thoushallnotpass")
    page.click("button:text('Log in')")

def order_your_robot():
    page = browser.page()
    page.goto("https://robotsparebinindustries.com/#/robot-order")
    close_annoying_modal()

def close_annoying_modal():
    page = browser.page()
    page.click("button:text('Yep')")

def fill_and_submit_order(order_content,robotParts):
    """Fills in the order content andclick the 'Submit' button"""
    page = browser.page()
    page.select_option("#head",str(order_content["Head"]))
    page.click("#id-body-" + str(order_content["Body"]))
    page.fill("input.form-control",order_content["Legs"])
    page.fill("#address",order_content["Address"])
    page.click("#preview")
    order_robot(order_content["Order number"])



def extract_model_info():
    """Extract model info and returns it as a dictionary"""
    page = browser.page()
    page.click("button:text('Show model info')")
    modelInfo = page.inner_html("#model-info")
    modelInfo = modelInfo.replace("<thead><tr><th>Model name</th><th>Part number</th></tr></thead><tbody><tr>","").replace("</tr></tbody>","").replace("</tr><tr>","|").replace("</td><td>",";").replace("</td>","").replace("<td>","")

    robotParts = {}

    for model in modelInfo.split("|"):
        robotParts[model.split(";")[1]] = model.split(";")[0]
    return robotParts

def order_robot(orderID):
    page = browser.page()
    page.click("#order")

    checkError = page.is_visible("div.alert-danger")

    while(checkError):
        page.click("#order")
        checkError = page.is_visible("div.alert-danger")

    create_pdf_receipt(orderID)

    page.click("#order-another")
    close_annoying_modal()

def create_pdf_receipt(orderID):
    page = browser.page()
    receipt_html = page.locator("#receipt").inner_html()
    page.locator("#robot-preview").screenshot(path="receipts/robot" + orderID + ".png")

    pdf = PDF()
    pdf.html_to_pdf(receipt_html + "<div><img = src=receipts/robot" + orderID + ".png></div>", "receipts/receipt" + orderID + ".pdf")
    os.remove("receipts/robot" + orderID + ".png")
    

def log_out():
    """Presses the 'Log out' button"""
    page = browser.page()  
    page.click("text=Log out")

    
