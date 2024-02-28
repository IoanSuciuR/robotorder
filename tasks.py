import logging 
import shutil
import os

from robocorp.tasks import task
from robocorp import browser

from RoboIncApp import open_the_intranet_website
from RoboIncApp import log_in
from RoboIncApp import order_your_robot
from RoboIncApp import fill_and_submit_order
from RoboIncApp import extract_model_info
from RoboIncApp import log_out

from Excel import download_excel_file
from Excel import get_orders
@task
def order_robots_from_RobotSpareBin():
    """
    Orders robots from RobotSpareBin Industries Inc.
    Saves the order HTML receipt as a PDF file.
    Saves the screenshot of the ordered robot.
    Embeds the screenshot of the robot to the PDF receipt.
    Creates ZIP archive of the receipts and the images.
    """
    logging.info("Starting process")
    process_configuration()
    open_the_intranet_website()
    log_in()
    order_your_robot()

    robotParts = extract_model_info()


    download_excel_file()
    orders = get_orders()



    process_orders(orders,robotParts)

    archived = shutil.make_archive("output/receipts", "zip", "receipts")
    if os.path.exists("receipts"):
        shutil.rmtree("receipts", ignore_errors=True)

    log_out()

    logging.info("End process")




def process_configuration():

    if os.path.exists("receipts"):
        shutil.rmtree("receipts", ignore_errors=True)
    if os.path.exists("receipts"):
        shutil.rmtree("receipts", ignore_errors=True)

    browser.configure(
        slowmo=0,
    )

def process_orders(orders,robotParts):
    for row in orders:
        fill_and_submit_order(row,robotParts)

