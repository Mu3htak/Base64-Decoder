import base64,sys
import argparse, binascii
from colorama import Fore

parser = argparse.ArgumentParser(description="Decode base64 format")
parser.add_argument('-d','--decode',nargs='*',required=True,help="Paste base64 string to decode")
args = parser.parse_args()

try:
    
    for i in args.decode:
        decodedbytes = base64.b64decode(i)
        decodedstr = str(decodedbytes, "utf-8")
        print("[%s] Decoded -> %s" %(Fore.RED + i + Fore.RESET,Fore.GREEN + decodedstr))
        sys.stdout.write(Fore.GREEN + Fore.RESET)
        sys.stdout.flush()
        
except binascii.Error:
    
    print("Bad Format -> [%s]" % (Fore.RED + i + Fore.RESET))
