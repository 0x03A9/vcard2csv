#!/usr/bin/env python3

"""Converts a contacts file exported from an old Nokia phone to a CSV file.

On old Nokia phones (e.g., Nokia 222) an address book entry consists only of two fields:
name and phone number.
A backup of the contacts can be created on a memory card from the phone's UI.
This results in a file named "backup.dat" with entries as follows:

BEGIN:VCARD
VERSION:2.1
N;ENCODING=QUOTED-PRINTABLE;CHARSET=UTF-8:;=
John=20Doe;;;
TEL;VOICE;CELL:+123456789
END:VCARD

That is, the format used is vCard 2.1 with Quoted-Printable encoding for the name.

This script converts files in the format described above to CSV files.
"""

import sys
import vobject

def convert():
    with open(sys.argv[1], "r") as infile, open(sys.argv[2], "w") as outfile:
        outfile.write("name,telephone\n")
        for vcard in vobject.readComponents(infile, allowQP=True):
            name = vcard.n.value.given
            # special handling for names containing a comma (,)
            if type(name) is list:
                name = ",".join(name)
            telephone = vcard.tel.value
            outfile.write("\"{}\",\"{}\"\n".format(name, telephone))

def usage():
    print("Usage:")
    print("    {} {} {}".format(sys.argv[0], "<infile>", "<outfile>"))

def main():
    if len(sys.argv) == 3:
        convert()
    else:
        usage()

if __name__ == "__main__":
    main()
