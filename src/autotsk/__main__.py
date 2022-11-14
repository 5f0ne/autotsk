import os
import sys

import argparse

from autotsk.Controller import Controller

def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True, help="Path to disk file")
    parser.add_argument("--result", "-r", type=str, default=os.path.join(".", "autotsk-result"), help="Path to result dir")
    args = parser.parse_args()

    c = Controller()
    c.printHeader(args.path)

    # Check if result folder exists
    if(not os.path.isdir(args.result)):
            os.mkdir(args.result)
    else:
        print("")
        print("Directory already exists: " + args.result)
        print("")
        c.printExecutionTime()
        exit()     

    print("")
    print("mmls Output")
    print("----------")
    print("")

    # Get available partitions with mmls
    os.popen("mmls " + args.path + " > " + os.path.join(args.result, "mmls.txt"))
    mmlsOutput = os.popen("mmls " + args.path).read()

    print(mmlsOutput)
    

    # Extract the partition entries from mmls output
    lines = mmlsOutput.split("\n")

    print("")
    print("")
    print("Extracting Offsets")
    print("----------")
    print("")

    partitionOffsets = []
    for line in lines:
        cols = line.split("  ")
        if(len(cols) == 6):
            col = cols[1].replace(" ", "")
            if(":" in cols[1] or (col != "--------" and col != "Meta")):
                clean = "".join(s.lstrip("0") for s in cols[2]).replace(" ", "")
                partitionOffsets.append(clean)
                print("Offset found: " + clean)
              
    
    print("")
    print("")
    print("")
    print("Applying TSK Commands")
    print("----------")
    print("")

    # With the extracted offsets, create fsstat and fls output
    count = 0
    for offset in partitionOffsets:
        print("fsstat and fls for offset: " + offset)
        os.popen("fsstat -o " + offset + " " + args.path + " > " + os.path.join(args.result, str(count) + "-" + offset + "-fsstat.txt"))
        os.popen("fls -r -p -o " + offset + " " + args.path + " > " + os.path.join(args.result, str(count) + "-" + offset + "-fls.txt"))
        count += 1

    print("")
    print("")
    print("")
    print("Result Location")
    print("----------")
    print("")
    print("Path: " + args.result)

    print("")
    c.printExecutionTime()

if __name__ == "__main__":
    sys.exit(main())
