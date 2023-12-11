import argparse 

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("--waitForPrinter", help="`True` to enter wait loop if printers not found", default='False')

args = parser.parse_args()

if args.waitForPrinter.lower() == 'true': 
	print("waitForPrinter true")
