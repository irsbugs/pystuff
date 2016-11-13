#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Floating_Point. template_l2_20.py based on template_master_l2.py
# Introduces: To highlight floating point issues and limitations.
#       https://docs.python.org/3/tutorial/floatingpoint.html
#       Before 2.7 (including Python 3.0), repr(f) would give up to 17
#       significant digits, as if formatted with %17g. An IEEE-754 floating
#       point value has 53 significant binary digits, which is approximately
#       16 decimal digits. 17 significant digits guarantee that each binary
#       value produce a different decimal value.
#
# TODO: Describe your program here so that its description will be displayed
# using help(). See pydocs https://docs.python.org/3/library/pydoc.html
# E.g. $ pydoc3 -p 1234 then in a browser http://localhost:1234/
#

# Template functions utilize modules. Import them now to avoid problems later.
# import modules    # Functions, St trings, Lists used in template:
import sys          # .version(), .hexversion(), .exit(), .argv .stdout.write()
#                   # .stdout.flush()
import os           # .sep, .getcwd()
import datetime     # .datetime.now().strftime() .datetime.utcnow().strftime()
#                   # .datetime.today()
import textwrap     # .TextWrapper()
import tempfile     # .TemporaryFile(), .gettempdir()
import time         # .time(), .sleep()
import locale       # .setlocale(), .currency()

# Modules that could be handy...
import decimal
import math
import random

# Program details variables.
_program_ = "Floating_Point"  # "template_l2_20.py"
_version_ = "1.0"
_date_ = "2016-10-25"
_author_ = "Ian Stewart"
_copyright_ = "© https://creativecommons.org/licenses/by/4.0/"
_description_ = ("Demonstrate floating-point arithmetic and \n"
                 "highlight some of its issues and limitations.")
_original_ = ("template_master_l2.py - Ian Stewart - October 2016.\n"
              "© https://creativecommons.org/licenses/by/4.0/")

# Global Constants and variables init values. Can be read within functions.
# Can be the default values for arguments of a function.
PYTHON_MIN_VERSION = "3.2"
debug = False
log = "log_{}.txt".format(_program_)
sample = 20
input_file = "./temp/some_data.txt"
output_file = "{}.csv".format(_program_)
timer_activated = 0

# Global variables that could be handy...
sep = os.sep
cwd = os.getcwd() + sep

# Check python is not below version 3. Prohibit running version 2.
if int(sys.version[:1]) < 3:
    print("Python version {} is not supported. \n"
          "Please restart using Python version 3 or higher. Exiting..."
          .format(sys.version.split(" ")[0]))
    sys.exit(1)


def messages(number=0):
    if number == 0:
        m = """
    Integers may be positive or negative and accurately perform the arithmetic
    operations of addition (+), subtraction (-), multiplication (*), floor
    division (//), modulus (%) and exponent (**).
    An integer data type may be verified using the type() function which will
    return <class 'int'>. E.g.
    a = 2**10000
    print(type(a))
    <class 'int'>
        """
        return m

    if number == 1:
        m = """
    Float is another class for numeric data. It is based on IEEE 754 standard
    for double-precision floating-point format using 64 binary bits (8 bytes).
    The storage of a number utilizes the 64 bits as follows:
    Sign bit: 1 bit (Bit63)
    Exponent: 11 bits (Bits 52 to 62)
    Significand precision: 53 bits (52 explicitly stored) (Bits 0 to 51)

    For more information see...
    https://en.wikipedia.org/wiki/Double-precision_floating-point_format
    https://en.wikipedia.org/wiki/IEEE_floating_point#IEEE_754-2008
    https://docs.python.org/3/tutorial/floatingpoint.html
        """
        return m

    if number == 2:
        m = """
    Floats are displayed in the following ways...
    1.0, -3.0, 0.0, -0.0, 1.2345, -1.2345e+20, 1.2e-5, nan, inf, -inf,
    3.141592653589793, -0.3333333333333333, 1.7976931348623157e+308, 1.0e-323,

    The type function verifies if the data type is a float. E.g.
    print(type(1.0))
    <class 'float'>
    An integer may be converted to a float using the float() function. E.g.
    a = 3 + 6
    print(type(a))
    <class 'int'>
    a = float(a)
    print(a)
    9.0
    print(type(a))
    <class 'float'>
    Multiplying an integer by any float provides a result that is a float type.
    E.g.
    b = 9 * 1.0
    print(type(b))
    <class 'float'>
        """
        return m

    if number == 3:
        m = """
    The 53 binary bits of significand precision normally convert to 17 decimal
    places. The 11 binary bits available for storing the exponent provide a
    maximum exponent value of 2**1024. This converts to a decimal exponent
    of 308. Thus...

    Maximum positive number is approximately 10**308
    Maximum negative number is approximately -10**308

    For the smallest numbers that may exist these may be smaller than 10**-308
    due to utilizing of "subnormal numbers" which increases the exponent to
    -323. Thus...

    Positive number closest to zero is 10**-323
    Negative number closest to zero is -10**-323

    For information on subnormal numbers see...
    https://en.wikipedia.org/wiki/Denormal_number
        """
        return m

    if number == 4:
        m = """
    The Binary64 method of storing floating point numbers may result in some
    decimal numbers not being able to be converted exactly to binary.

    Decimal floating point numbers use tenths, hundredths, thousandths, etc.
    of an integer after the decimal point.

    Binary floating point numbers use, halves, quarters, eigths, sixteenths,
    etc. of an integer after the binary point.
        """
        return m

    if number == 5:
        m = """
    A rational number is any number that can be expressed as the quotient or
    fraction p/q of two integers, a numerator p and a non-zero denominator q.

    8/1. 8 divided by 1 is 8. Thus all integers are rational numbers.
    1/2. 1 divided by 2 is a half or 0.5.
    8 could be consider to be the floating point value of 8.000000... with an
    infinte number of zeros. Likewise 0.5 could be considered to be
    0.500000000... with an infinite number of zeros. The infinitely-repeated
    digit sequence is called the repetend or reptend. If the repetend is a
    zero, this decimal representation is called a terminating decimal.

    1/3. 1 divided by 3 is one third or 0.3333333333333...
    The decimal representation of 1/3 has an infinately repeating 3. Thus some
    inaccuracy will exist when storing 1/3 in its decimal form as it is not
    possible to store the infinately repeating 3's.

    A similar issue exists with 2/3 which in it decimal form is 0.6666666...
    with the 6 infinately repeating. One solution is to round the value after
    a desired amount of resolution. E.g. 0.6666666667. Using rounded values
    may result in small descrepancies in the result of mathmatical operations.
        """
        return m

    if number == 6:
        m = """
    Rational numbers stored in binary form may also terminating in zeros or
    infinately repeating a 1 or a sequence of 1's and 0's.

    In the case of 1/10. One divided by ten is 0.1 in its decimal form. It is
    a terminating decimal.

    When 1/10 is in its binary form it is:
    0.0001100110011001100110011001100110011001100110011...
    After 0.0 there is an infinately repeating sequence of 0011. Thus 1/10
    can not be accurately stored in binary form.
        """
        return m


def main(sample=sample, log=log, in_file=input_file, out_file=output_file):
    """
    Main function that calls all other defined functions and statements.
    Edit this function to make your program...
    """
    message = "Program {} launched.".format(sys.argv[0])
    append_logfile(message, log)

    if debug: print("Program is starting...")

    # Call functions here...
    print("{} is executing...".format(_program_))

    print(messages(0))
    print(messages(1))
    input("Type return to continue...")
    print(messages(2))
    input("Type return to continue...")
    print(messages(3))
    input("Type return to continue...")
    print(messages(4))
    print("For an example of a decimal value as an exact binary value.")
    print("The fraction 5/8 in decimal is 0.625")
    print("This is 6/10 + 2/100 + 5/1000 = {}"
          .format(6 / 10 + 2 / 100 + 5 / 1000))
    print("Or... 625/1000 = {}".format(625 / 1000))
    print()
    print("The fraction 5/8 in binary is 0.101")
    print("This is 1/2 + 0/4 + 1/8 = 0.101 in binary.\n"
          "Equivalent to: 4/8 + 0/8 + 1/8 = 5/8. Equalling {} in decimal."
          .format(1 / 2 + 0 / 4 + 1 / 8))

    input("\nType return to continue...")
    print()
    print("As an example of a decimal that doesn't have an exact binary value")
    print("1/10 = 0.1 in decimal.")
    print("Python performs the division of 1 by 10 and stores this as a\n"
          "Binary64 floating point value. When Python is required to display\n"
          "this stored binary value then conversion to decimal and rounding\n"
          "is performed to display 0.1")
    print("1/10 = {}".format(1 / 10))
    print()

    print("However on some occasions the slight descrepancies between binary\n"
          "values and their displayed decimal values may be observed...")
    print("0.1 + 0.1 = {}".format(0.1 + 0.1))
    print("0.1 + 0.1 + 0.1 = {}".format(0.1 + 0.1 + 0.1))
    print("0.1 + 0.1 + 0.1 + 0.1 = {}".format(0.1 + 0.1 + 0.1 + 0.1))
    print("0.1 + 0.1 + 0.1 + 0.1 + 0.1 = {}"
          .format(0.1 + 0.1 + 0.1 + 0.1 + 0.1))
    print("0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 = {}"
          .format(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1))
    print("0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 = {}"
          .format(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1))
    print("0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 = {}"
          .format(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1))
    print("0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 = {}"
          .format(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1))
    print("0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 = {}"
          .format(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1))
    print()
    print("Notice that the rounding algorithm used in displaying the decimal\n"
          "value may not always return a result of just one decimal point.")

    input("\nType return to continue...")
    print()
    print(messages(5))

    input("\nType return to continue...")
    print()
    print(messages(6))
    input("\nType return to continue...")
    print()
    # Precision of 1/10th in binary
    # 1/10 in binary form repeats as 0011 sequence. 0.0001100110011...
    print("1/10 converted to binary with varying levels of precision...")
    print()
    for precision in range(4, 61, 8):
        total = 0.0
        bin_string = "0.0"
        for exponent in range(precision):
            if exponent % 4 == 0 or exponent % 4 == 1:
                total = total + 0 / 2**(exponent + 2)
                bin_string = bin_string + "0"
            if exponent % 4 == 2 or exponent % 4 == 3:
                total = total + 1 / 2**(exponent + 2)
                bin_string = bin_string + "1"
        print("{: >2d} binary bits: {}".format(precision + 1, bin_string))
        print("Returned in decimal form: {: <19}"
              .format(total))

    input("\nType return to continue...")
    print()
    print("Excessively large floats return inf for infinity.")

    print("Maximum positive float until positive infinity...")
    print("1.7976931348623156e+308 is {}".format(1.7976931348623157e+308))
    print("1.7976931348623157e+308 is {}".format(1.7976931348623157e+308))
    print("1.7976931348623158e+308 is {}".format(1.7976931348623158e+308))
    print("1.7976931348623159e+308 is {}".format(1.7976931348623159e+308))
    print("1.7976931348623160e+308 is {}".format(1.7976931348623160e+308))
    print("1.7976931348623161e+308 is {}".format(1.7976931348623161e+308))

    print()
    print("Excessively large integer overflows the float() function")
    print("Maximum positive integer **308 to float overload...")
    try:
        print("float(1 * 10**308) is {}".format(float(1 * 10**308)))
    except OverflowError as e:    
        print("float(1 * 10**308) is OverflowError: {}".format(e))

    try:
        print("float(2 * 10**308) is {}".format(float(2 * 10**308)))
    except OverflowError as e:    
        print("float(2 * 10**308) is OverflowError: {}".format(e))

    print()
    print("Maximum positive integer **307 to float overload...")

    try:
        print("float(16 * 10**307) is {}".format(float(16 * 10**307)))
    except OverflowError as e:    
        print("float(16 * 10**307) is OverflowError: {}".format(e))
    try:
        print("float(17 * 10**307) is {}".format(float(17 * 10**307)))
    except OverflowError as e:    
        print("float(17 * 10**307) is OverflowError: {}".format(e))
    try:
        print("float(18 * 10**307) is {}".format(float(18 * 10**307)))
    except OverflowError as e:    
        print("float(18 * 10**307) is OverflowError: {}".format(e))
    try:
        print("float(19 * 10**307) is {}".format(float(19 * 10**307)))
    except OverflowError as e:    
        print("float(19 * 10**307) is OverflowError: {}".format(e))

    append_logfile("Completed Floating-Point")

    if debug: print("Program is finished.")
    append_logfile("Program {} finished.".format(_program_))
    sys.exit(1)
    # ===== end of main function =====


def python_version_check():
    """
    Check the version of python used is at the minimum or above the value for
    PYTHON_MIN_VERSION.
    sys.hexversion are: aa (major) bb (minor) cc (micro) f0 (final release)
    E.g. 0xaabbccf0. 0x30502f0 is 3.5.2 (final release)
    """
    min_version_list = PYTHON_MIN_VERSION.split(".")
    # Truncate if the list is more the 4 items
    if len(min_version_list) > 4:
        min_version_list = min_version_list[:4]
    # Fill if the list is less then 4 items
    if len(min_version_list) == 1:
        min_version_list.append("0")
    if len(min_version_list) == 2:
        min_version_list.append("0")
    if len(min_version_list) == 3:
        min_version_list.append("f0")
    # Calculate the minimum version and an integer, which, when displayed as
    # hex, is easily recognised as the version. E.g. 0x30502f0 is 3.5.2
    min_version_value = 0
    for index, item in enumerate(min_version_list[::-1]):
        min_version_value = min_version_value + int(item, 16) * 2**(index * 8)
    if debug: print("Python Version Minimum:{}, Decimal:{}, Hex:{}"
                    .format(PYTHON_MIN_VERSION, min_version_value,
                            hex(min_version_value)))
    # test value and exit if below minimum revision
    if sys.hexversion < min_version_value:
        print("Python Version: {}. Required minimum version is: {}. Exiting..."
              .format(sys.version.split(" ")[0], PYTHON_MIN_VERSION))
        sys.exit(1)


def append_logfile(message=None, logfile=log, path=cwd):
    """
    Append a time stamp and message to a log file.
    Default to using the current working directory (cwd)
    Prefix with a time stamp.
    Example: 2016-10-18 10:37:38.306: A message
    If message exceeds 55 characters, then use textwrap to indent next line
    Uses: datetime
          textwrap
    """
    if message is None:
        return
    # Wrap the text if it is greater than 80 - 25 = 55 characters.
    # Indent 25 spaces to on left to allow for width of time stamp
    wrapper = textwrap.TextWrapper()
    wrapper.initial_indent = " " * 25
    wrapper.subsequent_indent = " " * 25
    wrapper.width = 80
    message = wrapper.fill(message).lstrip()

    if debug: print(path + logfile)
    f = open(path + logfile, "a")
    # Truncate the 6 digit microseconds to be 3 digits of milli-seconds
    stamp = ("{0:%Y-%m-%d %H:%M:%S}.{1}:".format(datetime.datetime.now(),
             datetime.datetime.now().strftime("%f")[:-3]))
    if debug: print(stamp + " " + message)
    f.write(stamp + " " + message + "\n")


def help():
    "Provide help on command line options available."
    print("Program: {0}, Version: {1}, Date: {2}, Author: {3}"
          .format(_program_, _version_, _date_, _author_))
    print("{}".format(_description_))
    print("Usage: {} [OPTION]".format(_program_))
    print("Arguments...")
    # print("  -s=, --sample=[VALUE]      Total iterations")
    print("  -h,  --help                Provide this help information.")
    print("  -d,  --debug               Provide additional information \n"
          "                             during program development.")
    # print("  -i=, --input=[FILE]        Input file")
    # print("  -o=, --output=[FILE]       Comma seperated values file")
    print("  -l=, --log=[FILE]          Provide a filename for logging.")
    print("")

    print("Copyright: {}\n".format(_copyright_))


if __name__ == "__main__":
    # Get command line options from sys.argv list
    for index, option in enumerate(sys.argv):
        if "-h" in option:
            help()
            sys.exit(1)

        if "-d" in option:
            debug = not debug

        # Collect string data from command line interface (cli) sys.argv list
        # -s = total_sample
        if "-s" in option:
            sample_list = sys.argv[index].split("=")
            if len(sample_list) > 1:
                sample = sample_list[1]

        if "-i" in option:
            input_list = sys.argv[index].split("=")
            if len(input_list) > 1:
                input_file = input_list[1]

        if "-o" in option:
            output_list = sys.argv[index].split("=")
            if len(output_list) > 1:
                output_file = output_list[1]

        # Provide for a log file. Changes file name assigned to "log" variable.
        if "-l" in option:
            log_list = sys.argv[index].split("=")
            if len(log_list) > 1:
                # Avoid complexity of log file in sub-directories. In cwd.
                if os.sep not in log_list[1]:
                    log = log_list[1]

    if debug: print("sys.argv list = {}".format(sys.argv))
    if debug: print("Variables: debug:{}, log:{}, input_file:{},"
                    "output_file:{}"
                    .format(debug, log, input_file, output_file))

    # Check the version of Python that is being run against Minimum version
    python_version_check()

    # Call main program, pass values from command line arguments, or variables
    # with their default values which may not have been modified by the cli.
    main(sample, log, input_file, output_file)

