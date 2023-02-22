# vcard2csv

When creating a backup of the contacts on an old Nokia phone (e.g., Nokia 222) one gets a file named `backup.dat` with entries as follows:

```
BEGIN:VCARD
VERSION:2.1
N;ENCODING=QUOTED-PRINTABLE;CHARSET=UTF-8:;=
John=20Doe;;;
TEL;VOICE;CELL:+123456789
END:VCARD
```

That is, the format used is [vCard 2.1](https://en.wikipedia.org/wiki/VCard) with [Quoted-Printable](https://en.wikipedia.org/wiki/Quoted-printable) encoding for the name.

The Python script `vcard2csv.py` provided here can be used to convert such files to CSV files.

Usage:

```
./vcard2csv.py <infile> <outfile>
```

Note that the package [VObject](https://eventable.github.io/vobject/) is required.
