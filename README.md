# structformatlength
structformatlength (sfl) is a Python tool for quick and dirty calculation of byte lengths.

This project is helpful when working with the Python standard library [struct](https://docs.python.org/3/library/struct.html) which is used to convert bytes to Python values through formats. Formats consist of the byte order and a composition of characters representing a certain type.

The byte order is ignored in the conversion process in this program and can therefore be omitted. Below is just a quick reference:

| Character | Byte order             | Size     | Alignment |
|-----------|------------------------|----------|-----------|
| @         | native                 | native   | native    |
| =         | native                 | standard | none      |
| <         | little-endian          | standard | none      |
| \>        | big-endian             | standard | none      |
| !         | network (= big-endian) | standard | none      |

Here's a list of all formats supported by sfl:

| Format | C Type             | Python type       | Standard size |
|--------|--------------------|-------------------|---------------|
| x      | pad byte           |                   |               |
| c      | char               | bytes of length 1 | 1             |
| b      | signed char        | integer           | 1             |
| B      | unsigned char      | integer           | 1             |
| ?      | _Bool              | bool              | 1             |
| h      | short              | integer           | 2             |
| H      | unsigned short     | integer           | 2             |
| i      | int                | integer           | 4             |
| I      | unsigned int       | integer           | 4             |
| l      | long               | integer           | 4             |
| L      | unsigned long      | integer           | 4             |
| q      | long long          | integer           | 8             |
| Q      | unsigned long long | integer           | 8             |
| e      |                    | float             | 2             |
| f      | float              | float             | 4             |
| d      | double             | float             | 8             |
| F      | float complex      | complex           | 8             |
| D      | double complex     | complex           | 16            |
| s      | char[]             | bytes             | variable      |
| p      | char[]             | bytes             | variable      |

The format is assumed to already be implemented in the code, so for the calculator to work, the right format is assumed. If a faulty one is provided, [a faulty result may follow](https://en.wikipedia.org/wiki/Garbage_in,_garbage_out).
