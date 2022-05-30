#!/usr/bin/env python
"""
An example of a step using MLflow and weight and biases 
"""
import argparse
import logging
import wandb


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)




    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()

    ######################
    # YOUR CODE HERE     #
    ######################


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="this steps clean the data")


    parser.add_argument(
        "--input_artifact", 
        type=str
        help="Fully-qualified name for the input artifact",
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type=signature
        help="Fully-qualified name for the output artifact",
        required=True
    )

    parser.add_argument(
        "-- output_type", 
        type=str
        help="type of the attribuute"
        required=True
    )

    
    args = parser.parse_args()


    "input_artifact": "sample.csv:latest",
                     "output_artifact": "clean_sample.csv",
                     "output_type": "clean_sample",
                     "output_description": "Data with outliers and null values removed",
                     "min_price": config['etl']['min_price'],
                     "max_price": config['etl']['max_price']

    go(args)
