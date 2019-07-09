#!/usr/bin/python

import os
import argparse
import json


model_dir = "model-specs"
parser = argparse.ArgumentParser()
parser.add_argument("--model", type=str, help="Model name")
parser.add_argument("--update", type=int, help="Update user's model code")
args = parser.parse_args()


def load_info():
    rv = {}
    info_file = os.path.join(model_dir, args.model, "info.json") 
    with open(info_file, "r") as fi:
        rv = json.load(fi)
    return rv


if __name__ == "__main__":
    info = load_info()
    print(info['name'])
    print(info['model'])
    print(info['modelFilename'])
    #COMMAND = f"./install-model.sh {info['name']} {info['model']} {args.update}"
    #os.system(COMMAND)
