#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import string
import random
import array
from sys import argv
import sys
import os

def shuffle_text(text):
  if isinstance(text, unicode):
    temp= array.array('u', text)
    converter= temp.tounicode
  else:
    temp= array.array('c', text)
    converter= temp.tostring
    random.shuffle(temp)
    return converter()

def ran_pwd(pwd_lengh, pwd_num_digits, pwd_num_specials, pwd_num_uppercase):
  lowercase = string.ascii_lowercase
  uppercase = string.ascii_uppercase
  digits = string.digits
  specials  = '=!.$%&/()=?¿¡^*{}-_,<>'
  length = pwd_lengh
  num_digits = pwd_num_digits
  num_specials = pwd_num_specials
  num_uppercase = pwd_num_uppercase
  #num_lowercase = pwd_num_lowercase
  rnd = random.SystemRandom()
  pwd = ''
  pwd = pwd + ''.join(rnd.sample(lowercase,1) + rnd.sample(uppercase,num_uppercase) \
  + rnd.sample(digits,num_digits) + rnd.sample(specials,num_specials))
  
  while len(pwd)<(length):
    pwd = pwd + ''.join(rnd.sample(lowercase,1))

  pwd = shuffle_text(pwd)
  return pwd

def main():
  #El argv siempre tiene 1 de len(argv) que es el nombre del mismo script.
  if len(argv) < 2:
    default=raw_input("\n\n  The default random password is 12 chars long, includes: \n 1 uppercase, 1 numbers, and 2 special chars, is that ok? y/n:..")
    if default == 'y' or default == '':
      password = ran_pwd(12,1,2,1)
      print "\n\n  Your random password is:  ", password
      print "\n\n\n"
    else:
      n_length = raw_input("\n\n Please enter password Length: ")
      print "\n"
      n_uppercase = raw_input("\n\n how many UPPERCASE chars?: ")
      print "\n"
      n_digits = raw_input("\n\n how many NUMBERS?: ")
      print "\n"
      n_specials = raw_input("\n\n how many SPECIAL chars?: ")
      print "\n"
      print "\n Your password will be %s chars long, with %s uppercase chars, %s numbers, and %s special chars\n" % (n_length, n_uppercase, n_digits, n_specials)
      password = ran_pwd(int(float(n_length)),int(float(n_uppercase)),int(float(n_digits)),int(float(n_specials)))
      print "\n\n  Your random password is:  ", password
      print "\n\n\n"


if __name__ == '__main__':
  main()
