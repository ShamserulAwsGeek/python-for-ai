
import argparse

parser = argparse.ArgumentParser()

#add command line arguments:
parser.add_argument("url", help="The URL of the file to download")
parser.add_argument("output", help="By which name the file should be saved")

#Parse the arguments
args = parser.parse_args()

#use arguments:
print(args.url)
print(args.output)
