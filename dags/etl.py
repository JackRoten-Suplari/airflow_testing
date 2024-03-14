from etlephant.etl import run_pipeline
from set_output import set_output

def run(customer):
    # Get gen config if etlephant is set to auto
    output = set_output() # TODO: override with seperate env if provided
    run_pipeline.airflow(customer.get("customer"), output)

if __name__== "__main__":
    run()
