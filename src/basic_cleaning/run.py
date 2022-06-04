#!/usr/bin/env python
"""
An example of a step using MLflow and weight and biases 
"""
import argparse
import logging
import wandb
import pandas as pd
import os


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    logger.info("Downloading artifact")
    artifact = run.use_artifact(args.input_artifact)
    artifact_path = artifact.file()

    logger.info("Cleaning data")

    df = pd.read_csv(artifact_path)
    df = df[ ( df["price"] >= args.min_price) & (df["price"] <= args.max_price) ]
    filename = args.output_artifact
    idx = df['longitude'].between(-74.25, -73.50) & df['latitude'].between(40.5, 41.2)
    df = df[idx].copy()
    df.to_csv(filename,index=False)

    artifact = wandb.Artifact(
        name=args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )
    artifact.add_file(filename)

    logger.info("Logging artifact")
    run.log_artifact(artifact)

    os.remove(filename)

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
        type=str,
        help="Fully-qualified name for the input artifact",
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type=str,
        help="Fully-qualified name for the output artifact",
        required=True
    )

    parser.add_argument(
        "--output_type", 
        type=str,
        help="type of the attribuute",
        required=True
    )

    parser.add_argument(
        "--output_description", 
        type=str,
        help="Data with outliers and null values removed",
        required=True
    )

    parser.add_argument(
        "--min_price", 
        type=float,
        help="Range of minimum price",
        required=True
    )

    parser.add_argument(
        "--max_price", 
        type=float,
        help="Range of maximum price",
        required=True
    )

    args = parser.parse_args()




    go(args)
