from cs.customer_scripts.lookupdate.update.run_pipeline import run
from datetime import datetime, timedelta

def set_output():
    """
    String with format of YYYY_MM_Refresh which will take today's
    date and set output equal to a month back
    :return: output: prev month refresh
    """
    today = datetime.now()
    # Hack method to get first day of chosen month
    # today = datetime(2024, 1, 1)
    first = today.replace(day=1)
    last_month = first - timedelta(days=1)
    output_string = str(last_month.year) + "_" + str(last_month.month) + "_Refresh"
    return output_string

customers = ["vitaminshoppe", "crownpackaging"]

def run():
    for customer in customers:
        run(customer)


if __name__== "__main__":
    run()