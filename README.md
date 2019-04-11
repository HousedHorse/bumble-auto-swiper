# Bumble Swiper
An autoswiper Python3 script for Bumble.

## Requirements

- Python3

If you follow the install instructions, these should be installed automatically:

- Selenium 3.141.0
- urllib 1.24.1

## Installation

**Disclaimer:** These instructions are for GNU/Linux!! They *should* work on MacOS. You might need to change your PATH.
**Windows users -- you're on your own!**

```
$ git clone https://github.com/HousedHorse/bumble-auto-swiper
$ cd bumble-auto-swiper
$ sudo make install
```

## Running

### After Installation

```
$ bumble-swiper <facebook-email> <facebook-password>
```

### Without Installation

Clone this repo and navigate to the correct directory, then proceed as follows:

```
$ make
$ python3 bumble-swiper.py <facebook-email> <facebook-password>
```
